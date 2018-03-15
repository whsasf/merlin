# owm-aide

Role to install  & configure Aide Security tool.
AIDE:
* AIDE is a host-based IDS, which scans the file system and logs the attributes of important files,directories, and devices. 
* Each time it runs, it compares its findings against the previous, "knowngood" data, and alerts you if something has changes.
* AIDE constructs a database of the files specified in AIDE.conf, AIDE's configuration file. The AIDE database stores various 
  file attributes including: permissions, inode number, user, group, file size, mtime and ctime, atime, growing size, number of 
  links and link name.

## Role configuration

* aide_admin_email- Email id of the admin who will get the Aide report mail.
* aide_cron_config (Default: Daily) - Specifies the cron job for Aide. Set the following values:
    - minute (Default: 0) - Minute when the job should run ( 0-59, *, */2, etc )
    - hour (Default: 0) - Hour when the job should run ( 0-23, *, */2, etc )
    - day (Default: *) - Day of the month the job should run ( 1-31, *, */2, etc )
    - month (Default: *) - Month of the year the job should run ( 1-12, *, */2, etc )
    - weekday (Default: *) - Day of the week that the job should run ( 0-6 for Sunday-Saturday, *, etc )
