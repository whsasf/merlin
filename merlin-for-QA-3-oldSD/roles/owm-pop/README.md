# owm-pop

Role to install owm-pop packages on a system.

## Installs the owm-mss packages

The following attributes are required:

* conf_server_name - hostname of the server where conf-server is installed. It is taken by the Ansible Playbook.
* emailmx_user information - defined in the 'group_vars/mx'.
* emailmx_version - defined in the 'group_vars/mx' file.
* owm_repo_url - defined in the 'group_vars/all' file.
