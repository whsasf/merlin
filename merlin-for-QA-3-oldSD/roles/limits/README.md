# limits

This role can be used to set user and group limits (ulimit).

- Ethernet interfaces
- Network routes

## Examples

Simple example that sets up specific limits for 'imail' user and 'support'
group, and sets default values for others.

```
    - hosts: myhost
      roles:
        - role: limits
          limits_scopes:
              - name: "imail"
                limits:
                 - soft nofile 65536
                 - hard nofile 65536
                 - soft nproc 100
                 - hard nproc 100
              - name: "@support"
                limits:
                 - soft nofile 256
                 - hard nofile 256
                 - soft nproc 20
                 - hard nproc 50
              - name: "root"
                limits:
                 - soft nofile 512
                 - hard nofile 512
                 - soft nproc 100
                 - hard nproc 200
              - name: "*"
                limits:
                 - soft nofile 128
                 - hard nofile 128
                 - soft nproc 200
                 - hard nproc 500
```

