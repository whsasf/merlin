# owm-recovery

Role to take recovery for directory,Cassandra metadata,Cassandra blobstore,mos and affinity manager from backup server.

## Prerequisites

Backup files should be present for components directory,Cassandra metadata,Cassandra blobstore,mos and affinity manager on backup server and respective backup date should be assign to respective backup date variable in roles/owm-recovery/vars/main.yml.

## Role configuration

Following attributes are required in group_vars

* backup_server_path(default:/opt/merlin/backup)- defined in 'group_vars/all' and it required for copying backup files from backup server
* emailmx_user information - defined in the 'group_vars/mx'
* cass_user information - defined in the 'group_vars/cassandra'
* nginx_user information - defined in the 'group_vars/affinity'
* owm_nginx_version(default:1.7.4) - defined in the 'group_vars/affinity' 
* cassandra_source_version(default:"2.0.12") - defined in the 'group_vars/cassandra'

Following attributes are required in roles/owm-recovery/vars/main.yml

* dirserv_backup_date(default:201509010510) - dirserv backup date should be in format YYYYMMDDHHMM and it required for recovery of dirserv.
* confserv_backup_date(default:20150831_2210) - confserv backup date should be in format YYYYMMDD_HHMM and it required for recovery of confserv.
* cassmeta_backup_date(default:20150831_2205) - cassandra metadat backup date should be in format YYYYMMDD_HHMM and it required for recovery of cassandra metadata.
* cassblob_backup_date(default:20150831_2205) - cassandra blobstore backup date should be in format YYYYMMDD_HHMM and it required for recovery of cassandra blobstore.
* affinity_backup_date(default:20150901_2355) - affinity backup date should be in format YYYYMMDD_HHMM and it required for recovery of affinity.
* mos_backup_date(default:20150831_2209) - mos backup date should be in format YYYYMMDD_HHMM and it required for recovery of mos.
 
