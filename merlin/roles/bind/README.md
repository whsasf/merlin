bind
====

An ansible role for installing and managing bind, acting as primary and/or secondary and/or forwarding nameserver.

Examples
--------

A sample playbook for installing a caching nameserver that forwards RBL requests to a local RBLDNS server/

```
- hosts: nameservers
  vars:
    bind_config_recursion: "yes"

    bind_config_forward_zones:
      - name: Domains forwarded to local RBLDNS server
        forwarders: [
          { address: '127.0.0.1', port: 1153 }
        ]
        forward: only
        zones:
          - dbl.dnsbl

  roles:
    - role: bind
```
