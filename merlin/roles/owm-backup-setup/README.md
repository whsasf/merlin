# owm-backup-setup

Role for setting up backup server and various component servers from which we are taking backup.

## Role configuration

Following attributes are required in group_vars

* backup_server_path(default:/opt/merlin/backup)- defined in 'group_vars/all' and it required for creating backup directory on backup server.
