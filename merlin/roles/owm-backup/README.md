# owm-backup

Role to take backup for directory,Cassandra metadata,Cassandra blobstore,mos and affinity manager on backup server.

## Host vars configuration

This variables needs to configured properly in host_vars/site1dir01, host_vars/site1dir02 etc for running dirserv,confserv and mos backup.Same will be followed for multiple site.

dirserv_backup:
   - minute: "0"
     hour: "0"
     day: "*"
     month: "*"
     weekday: "*"
  (Default : configure it for midnight) - Defined for cron job to run at specific interval for dirserv backup.

confserv_backup:
   - minute: "0"
     hour: "0"
     day: "*"
     month: "*"
     weekday: "*"
  (Default : configure it for midnight) - Defined for cron job to run at specific interval for confserv backup.
  
mos_backup:
   - minute: "0"
     hour: "0"
     day: "*"
     month: "*"
     weekday: "*"
  (Default : configure it for midnight) - Defined for cron job to run at specific interval for mos backup.
  
This variable needs to configured properly in host_vars/site1met01,host_vars/site1blob01 etc for running Cassandra backup.Same will be followed for multiple nodes and site.  

cassandra_backup:
   - minute: "0"
     hour: "0"
     day: "*"
     month: "*"
     weekday: "*"
  (Default : configure it for midnight) - Defined for cron job to run at specific interval for cassandra backup.

This variable needs to configured properly in host_vars/site1afnmss01, host_vars/site1mos01,host_vars/site1afnfailover01 etc for running Cassandra backup.Same will be followed for multiple nodes and site. 

affinity_backup:
   - minute: "0"
     hour: "0"
     day: "*"
     month: "*"
     weekday: "*"  
  (Default : configure it for midnight) - Defined for cron job to run at specific interval for affinity backup

## Role configuration

Following attributes are required in group_vars

* backup_server_path(default:/opt/merlin/backup)- defined in 'group_vars/all' and it required for copying backup files on backup server
* emailmx_user information - defined in the 'group_vars/mx'
* cass_user information - defined in the 'group_vars/cassandra'
* nginx_user information - defined in the 'group_vars/affinity'
* owm_nginx_version(default:1.7.4) - defined in the 'group_vars/affinity'
