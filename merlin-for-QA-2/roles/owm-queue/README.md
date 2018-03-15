# owm-queue

Role to install owm-queue packages on a system and maintenance queue.

## Host vars configuration

This variables needs to configured properly host_vars/site1que01 etc for queue maintenance.

* queue_maintenance:
   - minute: "1"
     hour: "0"
     day: "*"
     month: "*"
     weekday: "*"
   (default: Configure it for 00:01 AM ) defined for cron job to run at specific interval on queue node

## Installs the owm-queue packages

The following attributes are required:

* conf_server_name - hostname of the server where conf-server is installed. It is taken by the Ansible Playbook.
* emailmx_user information - defined in the 'group_vars/mx'.
* emailmx_version - defined in the 'group_vars/mx' file.
* owm_repo_url - defined in the 'group_vars/all' file.
* mx_maintenance(default: true) - Defined in 'group_vars/mx' and It is required for maintenance.
