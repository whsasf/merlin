# nrpe

Ansible role to handle the installation of the Nagios NRPE Daemon.

## Role Information

This role gives you the ability to deploy global plugins.
This can be done by putting plugins into [`files/plugins`](files/plugins)

## Role Variables

  * *nrpe_bind_address*: 127.0.0.1
  * *nrpe_port*: 5666
  * *nrpe_allowed_hosts*: 127.0.0.1
  * *nrpe_pid*: /var/run/nrpe/nrpe.pid
  * *nrpe_user*: nrpe
  * *nrpe_group*: nrpe
  * *nrpe_repo_redhat*: epel
  * *nrpe_service*: nrpe
  * *nrpe_dir*: /etc/nagios
  * *nrpe_include_dir*: /etc/nrpe.d

## Dependencies

epel

## Example Playbook

```yaml
- hosts: servers
  roles:
     - nrpe
   vars:
     nrpe_allowed_hosts: 192.168.0.1,127.0.0.1
```

