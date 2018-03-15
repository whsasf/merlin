# owm-mta

Role to install owm-mta packages on a system and maintenance mta.

## Role configuration

## Host vars configuration

This variables needs to configured properly host_vars/site1spm01 etc for mta maintenance.

* mta_maintenance:
   - minute: "1"
     hour: "0"
     day: "*"
     month: "*"
     weekday: "*"
  (default: Configure it for 00:01 AM)-Defined for cron job to run at specific interval on mta node

## Installs the owm-mta packages

The following attributes are required:

* conf_server_name - hostname of the server where conf-server is installed. It is taken by the Ansible Playbook.
* emailmx_user information - defined in the 'group_vars/mx'.
* emailmx_version - defined in the 'group_vars/mx' file.
* owm_repo_url - defined in the 'group_vars/all' file.
* mx_maintenance(default: true) - Defined in 'group_vars/mx' and It is required for maintenance.
