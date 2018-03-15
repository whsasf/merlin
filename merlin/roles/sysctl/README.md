# sysctl

Role which helps to manage the `sysctl` configuration.

# Example Playbook

```
---
- hosts: all
  vars:
    sysctl_config:
      kernel.sysrq: 1
      net.ipv4.tcp_syncookies: 1
  roles:
    - sysctl
```

# Role variables

List of variables used by the role:

```
# Default sysctl configuration
sysctl_config: {}

# Default sysctl.conf location
sysctl_config_location: /etc/sysctl.conf
```
