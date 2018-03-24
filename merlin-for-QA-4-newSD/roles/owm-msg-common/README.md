# owm-msg-common

Role to install owm-msg-common package on a system.

## Installs the owm-msg-common rpm 

It installs the owm-msg-common rpm required by the Mx components(i.e., MSS, IMAP, POP, MTA, QUEUE, EXT).

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
        - role: owm-msg-common
        - role: owm-imap
