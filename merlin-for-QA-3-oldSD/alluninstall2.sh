#!/bin/bash

#will clean everyting rexcept some config files nened.
#clear retry files 
rm -rf *.retry

hostnum=2
host1=10.49.58.121
host2=10.49.58.124
#host3=10.49.58.241
#host4=10.49.58.121
#host5=10.49.58.124

for (( i=1;i<=${hostnum};i++ ))
do
    eval tmp=\${host$i}
    echo "Doing cleanning job on $tmp ,please wait..."
		ssh root@$tmp "su - imail -c \"imboxdelete concuser@openwave.com\""
		ssh root@$tmp "systemctl stop sncr-registry"
		ssh root@$tmp "ps -ef|grep "sncr-registry"  |grep -v grep|awk '{print \$2}'|xargs kill -9"
		ssh root@$tmp "systemctl stop service-discovery"
    ssh root@$tmp "ps -ef|grep "service-discovery"  |grep -v grep|awk '{print \$2}'|xargs kill -9"
		ssh root@$tmp "systemctl stop service-discovery "
		ssh root@$tmp "ps -ef|grep "search"  |grep -v grep|awk '{print \$2}'|xargs kill -9"
		ssh root@$tmp "ps -ef|grep -iw imail|grep -v ssh|grep -v auto|awk '{print \$2}'|xargs kill -9"
		ssh root@$tmp "ps -ef|grep cass|grep -v ssh|grep -v auto|awk '{print \$2}'|xargs kill -9"
		ssh root@$tmp "systemctl stop elasticsearch"
		ssh root@$tmp "ps -ef|grep elasticsearch|grep -v ssh|grep -v auto|awk '{print \$2}'|xargs kill -9"
		ssh root@$tmp "rm -rf /opt/imail/*"
		ssh root@$tmp "rm -rf /opt/imail/.*"
		ssh root@$tmp "rm -rf /opt/owm"
		ssh root@$tmp "rm -rf /opt/owm/.*"
		ssh root@$tmp "rm -rf /opt/cass/*"
		ssh root@$tmp "rm -rf /opt/cass/.*"
		ssh root@$tmp "rm -rf /opt/sncr/*"
		ssh root@$tmp "rm -rf /opt/sncr/.*"
		ssh root@$tmp "ps -ef|grep cass|grep -v ssh|grep -v auto|awk '{print \$2}'|xargs kill -9"
		ssh root@$tmp "rpm -qa|grep owm-|grep -v auto|xargs rpm -e"
		ssh root@$tmp "rpm -qa|grep sncr|grep -v auto|xargs rpm -e"
		ssh root@$tmp "rpm -qa|grep -i platformtools|grep -v auto|xargs rpm -e"
		ssh root@$tmp "rpm -qa|grep -i elasticsearch|grep -v auto|xargs rpm -e"
		ssh root@$tmp "userdel -r imail"
		ssh root@$tmp "userdel -r cass"
		ssh root@$tmp "userdel -r owm"
		ssh root@$tmp "userdel -r sncr"
		ssh root@$tmp "groupdel  imail"
		ssh root@$tmp "groupdel  cass"
		ssh root@$tmp "groupdel  owm"
		ssh root@$tmp "groupdel  sncr"
		ssh root@$tmp "rm -rf /opt/merlin/*"
		ssh root@$tmp "rm -rf /opt/merlin/.*"
		
		
		# remove packages under /root/
		ssh root@$tmp "rm -rf sun-javadb*"
		ssh root@$tmp "rm -rf apache-cassandra*gz" 
		ssh root@$tmp "rm -rf jdk*rpm*" 
		
		
		# remove service under systemd
		ssh root@$tmp "rm -rf /etc/systemd/system/service-discovery.service" 
		ssh root@$tmp "rm -rf /etc/systemd/system/cassmeta.service" 
		ssh root@$tmp "rm -rf /etc/systemd/system/cassblob-cass.service"
		ssh root@$tmp "rm -rf /etc/systemd/system/cassblob-cass.service"
		
		#clean logs
		ssh root@$tmp "rm -rf /var/log/sncr*" 
		ssh root@$tmp "rm -rf /var/log/service-discovery" 
		ssh root@$tmp "rm -rf /var/log/logstash" 
		ssh root@$tmp "rm -rf /var/log/search*" 
		ssh root@$tmp "rm -rf /var/log/elasticsearch*" 
done
