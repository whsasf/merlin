#!/bin/sh
#
#  spamhaus-sync.sh				   v 3.1.2  27-oct-2010
#
#  This is a script to synchronize spamhaus.org zone files using rsync
#  for users of the Spamhaus DataFeed Rsync service.   Configure your
#  cron to call this script _every minute_.  Spamhaus Technology (SpamTeq)
#  do its best to keep your Spamhaus zones up to date, optimizing
#  usage of the rsync distribution infrastructure.  Only some files
#  will be rsynced at each minute, according to parameters tuned by
#  SpamTeq.
#
#  The script is organized so that new zones will be visible by your
#  local rbldnsd server only after successful termination of the 
#  synchronization and a verification of correctness.  If something goes 
#  wrong with the synchronization, rbldnsd will continue using the 
#  previous files until the next successful update, to prevent 
#  problems to your mail flow caused by corrupted files.
#
#  At this date the datasets are six: the four blocking lists 'sbl', 'pbl', 
#  'xbl' and 'dbl', and the two whitelists 'swl' and 'dwl'.  They
#  contain IP addresses except dbl and dwl that contain domains.
#  The rbldnsd working directory will contain symbolic links with these
#  names, pointing to files with the same name located in the 
#  directory used by this script ($WORKDIR).
#  For instance, assuming a hierarchy organized as follows:
#    /usr/local/dnsbl/rbldnsd/      rbldnsd working directory
#    /usr/local/dnsbl/spamhaus/     spamhaus' rsync working directory
#  one can (once for all) set up symbolic links in the following way:
#    % cd /usr/local/dnsbl/rbldnsd
#    % ln -s ../spamhaus/sbl sbl
#    % ln -s ../spamhaus/pbl pbl
#    % ln -s ../spamhaus/xbl xbl
#    % ln -s ../spamhaus/dbl dbl
#    % ln -s ../spamhaus/swl swl
#    % ln -s ../spamhaus/dwl dwl
#  (only use relative paths, as rbldnsd is usually running in a chrooted
#  environment with /usr/local/dnsbl as root directory, and would not
#  be able to deal with symlinks pointing to the full pathname).
#  Note: these are files, not directories!  Do not create directories
#  with these names.
#
#  For more detail, please refer to the Datafeed Rsync service
#  installation manual, available by accessing your account page
#  at the SpamTeq web site.
#
#  Users of Solaris and other legacy varieties of Unixes may wish to
#  change the shell in the first line into /bin/ksh or /bin/bash
#  in case of errors due to portability problems.  Please report us
#  any portability problem.
#
#  Spamhaus Technology Ltd.
#  For support issues about the operation of this script: 
#  <datafeed-support@spamteq.com>

VERSION="3.1.2"
#################################################### CONFIGURATION SECTION
#  Change variables to suit your environment.
#  Email address that the script will use to notify about
#  problems (leave blank if you do not wish to receive
#  trouble notifications; to send to several addresses separate
#  them with commas, without any space).
TROUBLES="troubles@example.com"
#  Working directory: this is where the Spamhaus files are located
WORKDIR=/var/lib/rbldnsd
#  BL files to be synchronized; usually "sbl pbl dbl xbl swl dwl".  
#  Change only in case you do not need some of these files.
BLFILES="sbl xbl"
#  If you wish to use the more aggressive "policy" version of the
#  SBL set SBLPOLICY="1", otherwise leave it empty (SBLPOLICY=).
#  The policy version may contain usually short-lived "escalation" 
#  listings that could block some non-spam mail, and should be 
#  chosen only by organizations willing to accept some false positives
#  to the end of getting cooperation from networks with serious
#  spam problems.
SBLPOLICY=
#  Rsync server pool to use. At present we support two pools of servers:
#	na.dr.spamhaus.net	referring to servers in North America
#	eu.dr.spamhaus.net	referring to servers in Europe
#  Choose the server pool that you believe to be closer (in terms of
#  traveling times of Internet packets) to your geographical location.
#########  DO NOT LEAVE XX.dr.spamhaus.net!  THIS MUST BE CHANGED!
RSYNCPOOL="na.dr.spamhaus.net"      ### replace XX with either na or eu ###
#  If you have reasons to prefer one particular server in our pool,
#  you can place its IP in the following variable. If we remove that
#  IP from the pool, your preference will become ineffective.
#  At most one IP can be specified. Most users do not specify anything here.
RSYNCHOST_IP_PREFER=""
#  If you have reasons to avoid at all costs one particular server in
#  our pool, you can place its IP in the following variable. 
#  At most one IP can be specified. Most users do not specify anything here.
RSYNCHOST_IP_AVOID=""
#  Rsync command options.  Please handle with care if you need to
#  change something; when in doubt, please contact us.
#  Do NOT specify the -B/-block-size=SIZE option (the script handles that).
#  Do NOT specify the -z/--compress option.
#  If you use --bwlimit=xx, do not go below 16 (already dangerously low),
#     --bwlimit=32 is a safer minimum.
#     Do not use --bwlimit unless you really have to.
RSYNCOPTS="-L -t --timeout=50"
#  If you wish to do checksum verification (recommended), define VERIFY 
#  to be "1", otherwise leave it empty  (VERIFY=):
VERIFY=1
#
#  The following are standard Unix/Linux programs that this script needs.
#  You can leave these definitions unchanged if the programs are located
#  in the path seen by cron jobs.  Warning: quite often, /usr/local/bin, 
#  /opt/bin etc are not in the cron path - try 'grep PATH /etc/crontab'
#  to verify the path.  In these cases, if you do not change the path,
#  you can give the full pathname to the command, for instance: 
#  RSYNC="/usr/local/bin/rsync" (as common for FreeBSD).
#
#			rsync command always needed
RSYNC="rsync"
#			cksum command needed if $VERIFY is defined
CKSUM="cksum"
#			mailx or Mail needed if $TROUBLES address is defined
#			Must accept mail subject passed with option -s.
MAILER="mailx"
#			host or dig is needed, one of them is enough.
#			If one of them is not available, define the
#			relative variable as a null string, such as DIG=""
HOST="host"
DIG="dig"
#			gzip command, if available, could be used to
#			speedup transfers for some zones (experimental
#			feature in the works).
GZIP="gzip"
#			Logfile (one line per rsync transaction):
LOGFILE="$WORKDIR/log"
#  Leaves diagnostic output in this directory:
OUTDIR="/tmp"
#  Location of timeslot and skipped times files.  These files need to survive 
#  between different runs of the script, but it is ok if a reboot wipes them.
TIMEFILE=/tmp/spamhaus-sync.tim
SKIPFILE=/tmp/spamhaus-sync.skp
#  Temporary and short-lived file containing list of processes:
PSTMPFILE=/tmp/spamhaus-sync.ps
################################################ END CONFIGURATION SECTION

NAME=`basename $0`
OUT=$OUTDIR/spamhaus-sync.out
ERR=$OUTDIR/spamhaus-sync-ERROR.out

#
#  Function to find in path and/or check existence of command.
#  Command name or full pathname passed as argument.
#  Full resulting pathname returned in $CMDPATH (if return value is 0).
#
cmd_location() {
	CMD=`basename $1`
	CMDPATH=""
	if [ $CMD = $1 ]
	then		# argument was not a full path, need to search
		for i in `echo $PATH | sed 's/^:/.:/
					    s/::/:.:/g
					    s/:$/:./
					    s/:/ /g'`
		do
			if [ -x $i/$1 ]
			then
				CMDPATH=$i/$1
				# Use the first found in user's path
				break
			fi
		done
		if [ -z "$CMDPATH" ]
		then
			echo "$1 not found in path ($PATH)" 1>&2
			return 1
		else
			return 0
		fi
	else		# argument is a full path already
		if [ ! -x $1 ]
		then					# not ok
			echo "$1 not found or not executable" 1>&2
			return 1
		else					# ok
			CMDPATH=$1
			return 0
		fi
	fi
}

#
#  check if we are running on Solaris
#
if [ `uname -s` = "SunOS" ]
then
	PS="ps -ef"
	if cmd_location gawk
	then
		DATEEPOCH="$CMDPATH 'BEGIN { print systime() }'"
	elif cmd_location nawk
	then
		DATEEPOCH="$CMDPATH 'BEGIN { print srand() }'"
	elif cmd_location perl
	then
		DATEEPOCH="$CMDPATH -e 'print time'"
	else
		DATEEPOCH="echo 0"
	fi
else
	PS="ps auxw"
	DATEEPOCH='date +%s'
fi

#
#  check existence of rsync command
#
if cmd_location $RSYNC
then
	RSYNC_PATH=$CMDPATH
else
	echo "$RSYNC not found" 1>&2
	echo "$RSYNC not found" > $ERR
	exit 1
fi

if [ $VERIFY ]
then
	#
	#  check existence of cksum command
	#
	if cmd_location $CKSUM
	then
		CKSUM_PATH=$CMDPATH
	else
		echo "$CKSUM not found" 1>&2
		echo "$CKSUM not found" > $ERR
		exit 1
	fi
fi

if [ $TROUBLES ]
then
	#
	#  check existence of mail command
	#
	if cmd_location $MAILER
	then
		MAILER_PATH=$CMDPATH
	else
		echo "$MAILER not found" 1>&2
		echo "$MAILER not found" > $ERR
		exit 1
	fi
fi

if [ $GZIP ]
then
	#
	#  check existence of gzip command
	#
	if cmd_location $GZIP
	then
		GZIP_PATH=$CMDPATH
	fi
fi

if [ $HOST ]
then
	#
	#  check existence of host command
	#
	if cmd_location $HOST
	then
		HOST_PATH=$CMDPATH
	fi
fi

if [ $DIG ]
then
	#
	#  check existence of dig command
	#
	if cmd_location $DIG
	then
		DIG_PATH=$CMDPATH
	fi
fi

#
#  exit if neither host or dig is available
#
if [ $DIG_PATH ]
then
	QUERY_PGM="dig"
else
	if [ $HOST_PATH ]
	then
		QUERY_PGM="host"
	else			# neither one is available
		cat /dev/null > $ERR
		if [ $HOST ]
		then
			echo "$HOST not found" 1>&2
			echo "$HOST not found" >> $ERR
		fi
		if [ $DIG ]
		then
			echo "$DIG not found" 1>&2
			echo "$DIG not found" >> $ERR
		fi
		exit 1
	fi
fi
#  $QUERY_PGM now is either "host" or "dig".

#
#  check existence of $WORKDIR and cd there
#
if [ ! -d $WORKDIR ]
then
	echo "Working directory $WORKDIR does not exist" 1>&2
	echo "Working directory $WORKDIR does not exist" > $ERR
	exit 1
fi
cd $WORKDIR
#
#  check if any of the BL files has been defined as a directory by mistake,
#  if yes then exit (this has been the reason for many support tickets!):
#
for BL in $BLFILES
do
    if [ -d $BL ]
    then
        if [ ! -n "$BL_DIR_DETECTED" ]
	then
	    cat /dev/null > $ERR
        fi
        echo "$WORKDIR/$BL can not be a directory! Remove it." 1>&2
        echo "$WORKDIR/$BL can not be a directory! Remove it." >> $ERR
        BL_DIR_DETECTED="1"
    fi
done
if [ -n "$BL_DIR_DETECTED" ]
then
    exit 1
fi

#  Current minute within the hour (00..59):
T=`date +"%M"`
#  Parameter $R for random timeslot selection (00..59):
if [ -s $TIMEFILE ]
then
    R=`cat $TIMEFILE`
    if [ -n "$R" ]
    then
	if [ ! \( "$R" -ge 0 -a "$R" -le 59 \) ]
	then	# out of range or not numeric, should not happen, remove file
	    rm -f $TIMEFILE
	    R=`expr $$ % 60`
	fi
    else	# empty? should not happen, remove file
	rm -f $TIMEFILE
	R=`expr $$ % 60`
    fi
else		# file not present, perhaps first run
    if [ -r /dev/urandom ]
    then
	R=`od -N4 -t u4 /dev/urandom | awk '{ print $2%60; exit }'`
    else
	R=`expr $$ % 60`
    fi
    if [ -n "$R" ]
    then
	if [ "$R" -ge 0 -a "$R" -le 59 ]
	then	# store it in file for later reuse
	    echo $R > $TIMEFILE
	else	# should not happen
	    R=`expr $$ % 60`
	fi
    else	# empty? should not happen, something went wrong with "od"
	R=`expr $$ % 60`
    fi
fi
#  Sleep $R seconds then start (to spread the load):
sleep $R

LOCKFILE="$WORKDIR/sync.lock"
#
#  check that no other copies are running.
#  It is crucial that we did not write anything to $OUT up to this point,
#  as another instance could be writing on it.
#
if [ -f $LOCKFILE ]
then				# lock file present, other instance at work
	if [ -s $LOCKFILE ]
	then			# file contents is check count
	    LOCKFILE_COUNT=`cat $LOCKFILE`
	else			# empty? should not be happening
	    LOCKFILE_COUNT=0
	fi
	LOCKFILE_COUNT=`expr $LOCKFILE_COUNT + 1`
	if [ -w $LOCKFILE ]	# update counter (if file still present & writable)
	then
	    echo $LOCKFILE_COUNT > $LOCKFILE
	fi
#	   add current time into the skipped times file, if not present already:
	if [ -s $SKIPFILE ]
	then
	    T_PRESENT=0
	    for TOLD in `cat $SKIPFILE`
	    do
		if [ "$T" -eq "$TOLD" ]
		then
		   T_PRESENT=1
		fi
	    done
	    if [ $T_PRESENT -eq 0 ]
	    then		# not present yet, add it
		echo "$T `cat $SKIPFILE`" > $SKIPFILE
	    fi
	else			# create it
	    echo "$T" > $SKIPFILE
	fi
	#  change $OUT as the other script may be still writing on the usual one
	OUT=$OUTDIR/spamhaus-sync-locked.out
	echo "spamhaus-sync.sh $VERSION started on `date`" > $OUT
	echo "Lock file $LOCKFILE found." >> $OUT
	echo "Lock file checked $LOCKFILE_COUNT time(s) so far (including now), at minutes:" >> $OUT
	cat $SKIPFILE >> $OUT
	echo " " >> $OUT
	echo "Another instance of $NAME is still running, or it terminated" >> $OUT
	echo "abnormally. If you are running $NAME via cron every minute as" >> $OUT
	echo "recommended, overlap of instances is expected to happen quite often, and" >> $OUT
	echo "there is nothing to worry about." >> $OUT
	echo " " >> $OUT
	echo "However, if the zone files have not been updated for one hour or" >> $OUT
	echo "more, and the check count in the fourth line of this message keeps" >> $OUT
	echo "growing, it could be that a previous instance terminated abnormally," >> $OUT
	echo "leaving the lock file behind it.  This script will now attempt to" >> $OUT
	echo "detect whether this is actually the case and, if yes, remove the lock." >> $OUT
	echo "However, this may fail, and in such a case you will have to remove the" >> $OUT
	echo "lock file manually by giving:" >> $OUT
	echo "		rm $LOCKFILE" >> $OUT
	echo "to resume synchronization." >> $OUT
	echo " " >> $OUT
	echo "The list of processes below should clarify the situation:" >> $OUT
	echo " " >> $OUT
	echo "- if there are two instances of $NAME and at least one" >> $OUT
	echo "  rsync process is present, then the previous copy is still running." >> $OUT
	echo "  The problem should go away by itself.  Wait some more time, and if" >> $OUT
	echo "  the problem persists then kill the rsync process(es)." >> $OUT
	echo " " >> $OUT
	echo "- if there is just one instance  of $NAME (the one that" >> $OUT
	echo "  composed this message!), then the previous copy terminated abnormally." >> $OUT
	echo "  In this case, if the problem is not fixed by this script run,  you will" >> $OUT
	echo "  probably have to remove manually the lock file as indicated above." >> $OUT
	echo " " >> $OUT
	echo "Processes:" >> $OUT
	echo " " >> $OUT
	$PS | egrep "$NAME|rsync" | grep -v "grep" > $PSTMPFILE 2>> $OUT
	cat $PSTMPFILE >> $OUT 2>&1
	if [ `wc -l < $PSTMPFILE` -eq 1 ]
	then		# just one process (this one), remove the lock
	    echo " " >> $OUT
	    echo "Since only one process was found (the one that composed this message)," >> $OUT
	    echo "the lockfile is now automatically removed and this should solve the problem." >> $OUT
	    echo "This is an emergency action (normally it should not be necessary)." >> $OUT
	    rm -f $LOCKFILE 2>> $OUT
	    NOTIFY="Emergency removal of lockfile"
	else
	    echo " " >> $OUT
	    echo "This copy of $NAME now quits without doing anything." >> $OUT
	fi
	rm -f $PSTMPFILE 2>> $OUT
	echo " " >> $OUT
	if [ $TROUBLES ]
	then
	    if [ `expr $LOCKFILE_COUNT % 60` -eq 0 ]
	    then
		echo "This report is mailed every 60 consecutive failed attempts." >> $OUT
		echo " " >> $OUT
		$MAILER -s "Persistent lock file preventing Spamhaus synchronizations" $TROUBLES < $OUT
	    fi
	fi
	#		Locked file exit:
	if [ -n "$NOTIFY" ]
	then					# some trouble occurred
		if [ $TROUBLES ]
		then
			$MAILER -s "$NOTIFY" $TROUBLES < $OUT
		fi
		exit 1
	fi
	exit
fi

#
#  Real work starts here
#
echo "spamhaus-sync.sh $VERSION started on `date`" > $OUT
echo "synchronizing files in $WORKDIR" >> $OUT

# create lock file and set up for clean up in case of externally-induced
# termination:
echo "0" > $LOCKFILE
trap 'rm -f $LOCKFILE ; exit 1' 1 2 3 15

echo "rsync command location: $RSYNC_PATH" >> $OUT
if [ $VERIFY ]
then
	echo "cksum command location: $CKSUM_PATH" >> $OUT
fi
if [ $TROUBLES ]
then
	echo " mail command location: $MAILER_PATH" >> $OUT
fi
if [ $GZIP_PATH ]
then
	echo " gzip command location: $GZIP_PATH" >> $OUT
else
	echo "gzip is not available" >> $OUT
fi
echo "rsync options: $RSYNCOPTS" >> $OUT
echo "epoch time obtained using: $DATEEPOCH" >> $OUT

#
#  get rsync server IPs to try:
#
if [ $QUERY_PGM = "host" ]
then
	echo " host command location: $HOST_PATH" >> $OUT
	LISTIP=`$HOST_PATH $RSYNCPOOL | awk 'BEGIN { ORS = " " } {if ( $0 ~ /^'"$RSYNCPOOL"'/ ) {print $NF}}'`
	echo "rsync servers (before ordering): $LISTIP" >> $OUT
elif [ $QUERY_PGM = "dig" ]
then
	echo "  dig command location: $DIG_PATH" >> $OUT
	LISTIP=`$DIG_PATH $RSYNCPOOL | awk 'BEGIN { ORS = " " } $1 == "'"$RSYNCPOOL"'." && $4 == "A" {print $5}'`
	echo "rsync servers (before ordering): $LISTIP" >> $OUT
else	# it should never happen
	LISTIP=$RSYNCPOOL
	echo "rsync servers called by name ($LISTIP)" >> $OUT
fi
#
#  reorder them according to preferences (if any).  Also filter away any
#  non-IP string that may have sneaked in erroneously (it should not happen).
#
LISTIP1=""
LISTIP2=""
for IP in $LISTIP
do
	IPVERIFIED=`echo $IP | awk '{if ( $1 ~ /^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$/ ) {print $1}}'`
	if [ -n "$IPVERIFIED" ]
	then				# it looks like a good IP
		if [ "$IPVERIFIED" = "$RSYNCHOST_IP_PREFER" ]
		then
			LISTIP1="$LISTIP1$IPVERIFIED "
		elif [ "$IPVERIFIED" != "$RSYNCHOST_IP_AVOID" ]
		then
			LISTIP2="$LISTIP2$IPVERIFIED "
		fi
	fi
done
if [ \( -z "$LISTIP1" \) -a \( -z "$LISTIP2" \) ]
then
	NOTIFY="No IPs found for pool $RSYNCPOOL"
	echo "PROBLEM: no IPs found for pool $RSYNCPOOL" >> $OUT
	echo " " >> $OUT
	if [ $QUERY_PGM = "host" ]
	then
		echo "Output of $HOST_PATH $RSYNCPOOL :" >> $OUT
		$HOST_PATH $RSYNCPOOL >> $OUT
	elif [ $QUERY_PGM = "dig" ]
	then
		echo "Output of $DIG_PATH $RSYNCPOOL :" >> $OUT
		$DIG_PATH $RSYNCPOOL >> $OUT
	fi
	LISTIP=""
	BLFILES=""	# to skip the following loop altogether
else			# OK
	LISTIP="$LISTIP1 $LISTIP2"
	echo "rsync servers ( after ordering): $LISTIP" >> $OUT
fi

#
#  did we skip some times due to a previous copy locking for
#  one minute or more?
if [ -s $SKIPFILE ]
then	# some previous times were skipped due to locks
	# and we will now consider them too
	SKIPTIMES="`cat $SKIPFILE`"
	echo "Also considering previous skipped minutes:" >> $OUT
	echo "$SKIPTIMES" >> $OUT
	# make $SKIPFILE an empty file so that these times will not
	# be considered again:
	cat /dev/null > $SKIPFILE
	# if $SKIPFILE remains empty up to the end it will be removed
	# (other processes may write on it in the meanwhile!)
else	# file absent or empty
	SKIPTIMES=""
	echo "No previous skipped minutes to consider." >> $OUT
fi

#
#  do rsync and installation of all BLs one by one, separately
#
for BL in $BLFILES
do
    echo "Deciding whether to start $BL synchronization .." >> $OUT
    if [ -s $BL ]
    then		# file is present, as it should.
			# read parameters in #RSYNC: line
	RSYNC_BL_PARS=`sed '5q' $BL |\
	    awk '$1 == "#RSYNC:" { print $2 " " $3 " " $4 " " $5 " " $6 " " $7 }'`
	echo "rsync parameters found in $BL: $RSYNC_BL_PARS" >> $OUT
	S=`echo $RSYNC_BL_PARS | awk '{print $1}'`
	G=`echo $RSYNC_BL_PARS | awk '{print $2}'`
	W=`echo $RSYNC_BL_PARS | awk '{print $3}'`
	Z=`echo $RSYNC_BL_PARS | awk '{print $4}'`
	B=`echo $RSYNC_BL_PARS | awk '{print $5}'`
	BZ=`echo $RSYNC_BL_PARS | awk '{print $6}'`
    else		# defaults, and emit warning
	echo "File $BL not present, rsync will transfer whole file!"  >> $OUT
	echo "You will receive this message only once for each BL,"   >> $OUT
	echo "when the service is started for the first time."        >> $OUT
	echo "If you keep receiving it, there is a problem: BL files" >> $OUT
	echo "are removed from $WORKDIR after rsyncing."              >> $OUT
	echo "Rsync can not work properly if files are removed."      >> $OUT
	NOTIFY="$BL file not present, rsync transfering whole file"
	S=0
	G=1
	W=1
	Z=0
	B=0
	BZ=0
    fi
    if [ ! \( -n "$S" -a -n "$G" -a -n "$W" -a -n "$Z" -a -n "$B" -a -n "$BZ" \) ]
    then			# some parameter was not found
	S=0
	G=1
	W=1
	Z=0
	B=0
	BZ=0
    fi	
    if [ $W -lt 1 -o $G -lt 1 ]
    then			# this should not happen ever
	echo "Wrong rsync parameters for $BL: /$S/$G/$W/$Z/$B/$BZ/."  >> $OUT
	ls -la >> $OUT
	echo "This should not happen: please notify support." >> $OUT
	NOTIFY="Wrong rsync parameters for $BL"
	S=0
	G=1
	W=1
	Z=0
	B=0
	BZ=0
    fi
    RW=`expr $R % $W`   # random spread in 0..$W-1
    DOIT="n"
    DELAYED=" "
#	check current time:
    if [ `expr \( $T - $S - $RW \) % $G` -eq 0 ]
    then
	echo "$BL scheduled for synchronization at this minute." >> $OUT
	DOIT="y"
	DELAYED="n"
    fi
#	check previous times (if any):
    for T1 in $SKIPTIMES
    do
	if [ `expr \( $T1 - $S - $RW \) % $G` -eq 0 ]
	then
	    echo "$BL synchronization delayed from previous minute $T1, rescheduled." >> $OUT
	    DELAYED="d"
	    DOIT="y"
	fi
    done
    if [ $DOIT != "y" ]
    then
	echo "$BL not scheduled for synchronization now." >> $OUT
    else			# go for it
	echo "Synchronization of $BL will now be started." >> $OUT
	#
	#  selection of special variants
	#
	if [ $BL = "sbl" ]
	then
	    if [ $SBLPOLICY ]
	    then			# adjust URL to fetch sbl-policy
		BLSYNC="sbl-policy"
		echo "sbl-policy version selected" >> $OUT
	    else
		BLSYNC=$BL
	    fi
	else
	    BLSYNC=$BL
	fi
	#
	#  can we try the gzipped version?  what rsync blocksizes?
	#
	if [ -n $GZIP_PATH -a $Z -eq 1 ]
	then				# yes, try gzipped version
	    RSYNC_GZ=1
	    BLSYNC=$BL".gz"
	    if [ $BZ -ge 128 ]
	    then
		RSYNCOPTS_BL="--block-size=$BZ"
	    else
		RSYNCOPTS_BL=""
	    fi
	    FILE=$BL.import.gz
	    ZONE=$BL.gz
	else				# no, regular version
	    RSYNC_GZ=0
	    if [ $B -ge 128 ]
	    then
		RSYNCOPTS_BL="--block-size=$B"
	    else
		RSYNCOPTS_BL=""
	    fi
	    FILE=$BL.import
	    ZONE=$BL
	fi
	#
	#  make a backup
	#
	if [ -f $ZONE ]
	then
	    cp -p $ZONE $FILE 2>> $OUT
	else
	    echo dummy > $FILE
	fi
	#
	#  synchronize file
	#
	RSYNC_ATTEMPTS=0
	FAILURE=-1
	for RSYNCHOST_IP in $LISTIP
	do
	    if [ $RSYNC_ATTEMPTS -lt 2 -a $FAILURE -ne 0 ]	# we try two IPs at most
	    then
		RSYNCURL="$RSYNCHOST_IP::rbldnsd/$BLSYNC"
		READING0=`eval $DATEEPOCH`
		TIMESTART=`date -u "+%e-%b-%Y %H:%M:%S UTC"`
		$RSYNC $RSYNCOPTS $RSYNCOPTS_BL $RSYNCURL $FILE > $OUTDIR/rsync.out 2>> $OUT
		FAILURE=$?
		READING=`eval $DATEEPOCH`
		ELAPSED=`expr $READING - $READING0`
		if [ $FAILURE -eq 0 ]
		then				# all well
		    FILESIZE=`ls -l $FILE | awk '{print $5}'`
		    echo "$BLSYNC rsynced successfully from $RSYNCHOST_IP, size=$FILESIZE, $ELAPSED s" >> $OUT
		else				# we have got a failure
		    echo "Failed to rsync $BLSYNC from $RSYNCHOST_IP, $ELAPSED s" >> $OUT
		    if grep 'contact Spamhaus' $OUTDIR/rsync.out >/dev/null 2>> $OUT
		    then				# no permission from this IP
			echo "This IP address is not permitted to access the Datafeed service" >> $OUT
			NOTIFY="Unauthorized access to Spamhaus Datafeed service"
		    else				# some other less trivial error
			echo "$RSYNC $RSYNCOPTS $RSYNCOPTS_BL $RSYNCURL $FILE FAILED with rsync exit code $FAILURE" >> $OUT
			#  this will be notified only if it occurs with both the IPs we are trying
			mv -f $FILE $FILE.failed 2>> $OUT
		    fi
		    FILESIZE=0
		fi
		printf "%24s %1s %-10s %-18s %9d %5d %5d\n" "$TIMESTART" $DELAYED $BLSYNC $RSYNCHOST_IP $FILESIZE $ELAPSED $FAILURE >> $LOGFILE
	    fi
	    RSYNC_ATTEMPTS=`expr $RSYNC_ATTEMPTS + 1`
	done
	if [ $FAILURE -ne 0 ]
	then					# both attempts failed
	    if [ -z "$NOTIFY" ]
	    then				# not a "access not permitted" error
		NOTIFY="rsync for $BL failed"	# report it
	    fi
	    echo "see http://www.samba.org/ftp/rsync/rsync.html for meaning of exit code $FAILURE" >> $OUT
	    echo "rsync for $FILE unsuccessfully terminated on `date`" >> $OUT
	else
	    echo "rsync for $FILE successfully terminated on `date`" >> $OUT
	    ls -l $ZONE $FILE >> $OUT 2>&1
	    #
	    #  sanity checks
	    #
	    #  verify that file is not empty
	    if [ ! -s $FILE ]
	    then
		echo "$FILE file is empty" >> $OUT
		NOTIFY="$FILE file is empty"
		mv -f $FILE $FILE.empty 2>> $OUT
		continue				# directly skip to next $BL
	    fi
	    #
	    #  decompress file
	    #
	    if [ $RSYNC_GZ -eq 1 ]
	    then
		$GZIP_PATH -d -c $FILE > $BL.import 2>> $OUT
		#  we now redefine:
		FILE=$BL.import
		ZONE=$BL
	    fi
	    #  verify that last line (checksum) is present
	    #  (note: grep -s or -q options to be avoided for portability)
	    if tail -1 $FILE | grep CKSUM > /dev/null 2>> $OUT
	    then
		:
	    else
		echo "Last line of $FILE is:" >> $OUT
		tail -1 $FILE >> $OUT
		echo "and does not contain the string CKSUM as it should." >> $OUT
		NOTIFY="$FILE file does not contain CKSUM"
		mv -f $FILE $FILE.failed 2>> $OUT
		continue				# directly skip to next $BL
	    fi
	    #  verify checksum
	    if [ $VERIFY ]
	    then
		CRC0=`tail -1 $FILE | awk '{print $3}'`
		CRC1=`sed '$d' $FILE | $CKSUM | awk '{print $1}'`
		if [ "$CRC0" = "$CRC1" ]
		then
		    echo "CRC verification for $FILE was successful." >> $OUT
		else
		    echo " CRC checksum in file: $CRC0" >> $OUT
		    echo "Computed CRC checksum: $CRC1" >> $OUT
		    echo "Checksums differ -- file corruption" >> $OUT
		    NOTIFY="$FILE: checksum error"
		    mv -f $FILE $FILE.failed 2>> $OUT
		    continue				# directly skip to next $BL
		fi
	    else
		echo "CRC verification for $FILE was skipped." >> $OUT
	    fi
	    #
	    #  put into production if changed
	    #
	    if cmp -s $ZONE $FILE 2>> $OUT
	    then
		echo "no changes for $BL" >> $OUT
		rm -f $FILE 2>> $OUT
	    else
		# move quickly into production:
		echo "zone $BL changed, moved into production .." >> $OUT
		mv -f $FILE $ZONE 2>> $OUT
		if [ $RSYNC_GZ -eq 1 ]
		then
		    mv -f $FILE.gz $ZONE.gz 2>> $OUT
		fi
	    fi
	fi
	echo "Synchronization of $BL terminated." >> $OUT
    fi
done

#
#  Remove the skipped times file if present AND if it was also
#  present when this instance was started (otherwise, the file may have
#  been created as the result of this instance locking for a long time,
#  and so the next instance will need it!) AND if no other process wrote
#  on it while this instance was executing.
#
if [ -n "$SKIPTIMES" ]
then
    echo "This run also considered previous skipped times." >> $OUT
    if [ -f "$SKIPFILE" ]
    then
	echo "Skipped times file is present, checking whether to remove it .." >> $OUT
	if [ -s "$SKIPFILE" ]
	then	# some other process wrote on it
		echo "No, it is not empty due to other instances writing on it, not removed:" >> $OUT
		cat $SKIPFILE >> $OUT
	else	# empty, can be removed
		echo "Yes, it remained untouched, removing it ($SKIPFILE)" >> $OUT
		rm -f $SKIPFILE 2>> $OUT
	fi
    else
	echo "However, the skipped times file is not present any more." >> $OUT
    fi
fi
#
#  Release the lock
#
echo "Removing lock file $LOCKFILE" >> $OUT
rm -f $LOCKFILE 2>> $OUT
echo "exiting on `date`" >> $OUT
#
#  If problems exit with error and notify user.  If there were
#  many errors, the subject line will reflect the last one, but
#  the email body will contain all the infos.
#
if [ -n "$NOTIFY" ]
then					# some trouble occurred
	if [ $TROUBLES ]
	then
		$MAILER -s "$NOTIFY" $TROUBLES < $OUT
	fi
	exit 1
fi
exit 0
