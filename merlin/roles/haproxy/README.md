# haproxy

A role to setup haproxy. The role may seem complex but it is to cover the
various scenarios in which haproxy is used in a typical deployment.

## Examples

```
- hosts: web-lbs
  vars:
    haproxy_frontends:
    - name: 'fe-http'
      ip: '127.0.0.1'
      port: '80'
      maxconn: '1000'
      default_backend: 'be-http'
    haproxy_backends:
    - name: 'be-http'
      description: 'Backend HTTP servers'
      servers:
        - name: 'somehost'
          ip: '192.168.1.100'
          port: '80'
        - name: 'somehost'
          ip: '192.168.1.101'
          port: '80'
  roles:
    - haproxy
```
