# owm-confserv

Role to install owm-confserv package on a system.

## Role configuration

* conf_cache_server (default: 0) - This param indicates whether deploy confcacheserv here
* domain_name (default: openwave.com) - Provide any valid domain name

## Installs the owm-confserv rpm

It installs the owm-confserv rpm.

The following attributes are required:

* conf_server_name - hostname of the server where conf-server is installed. It is taken by the Ansible Playbook.
* emailmx_user information - defined in the 'group_vars/mx'.
* emailmx_version - defined in the 'group_vars/mx' file.
* owm_repo_url - defined in the 'group_vars/all' file.
