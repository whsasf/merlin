# owm-sur-common

Role to install owm-sur-common package on a system.

## Installs the owm-sur-common rpm 

It installs the owm-sur-common rpm required by the Mx components(i.e., dirserv, dircache).

The following attributes are required:

* conf_server_name - hostname of the server where conf-server is installed. It is taken by the Ansible Playbook.
* emailmx_user information - defined in the 'group_vars/mx'.
* emailmx_version - defined in the 'group_vars/mx' file.
* owm_repo_url - defined in the 'group_vars/all' file.

This role can be added as given below:

Example:

    ---
    - hosts: directory
      roles:
        - role: common
        - role: owm-sur-common
        - role: owm-dirserv
        - role: owm-dircacheserv
