# owm-mx-common

Role to install owm-common package on a system.

## Role configuration

* conf_server_admin_port (default: 5002) - sets the specified admin port for confserv
* conf_server_port (default: 5003) - sets the specified port for confserv

## Installs the owm-common rpm 

It installs the owm-common rpm required by the Mx components(i.e., Conf-Server, Directory, IMAP, POP, MTA, QUEUE, EXT).

The following attributes are required:

* conf_server_name - hostname of the server where conf-server is installed. It is taken by the Ansible Playbook.
* emailmx_user information - defined in the 'group_vars/mx'.
* emailmx_version - defined in the 'group_vars/mx' file.
* owm_repo_url - defined in the 'group_vars/all' file.

This role can be added as given below:

Example:

    ---
    - hosts: fep
      roles:
        - role: common
        - role: owm-mx-common
        - role: owm-mx-imap
