dns
================

Ansible role for configuring DNS

# Examples :
```
- hosts: all
  roles: 
  - role: dns
    dns_domain: localdomain
    dns_nameservers: ['127.0.0.1', '8.8.8.8']

- hosts: all
  roles:
  - role: dns
    dns_nameservers: ['8.8.8.8']  
    dns_searches: "localdomain someotherdomain"

```
