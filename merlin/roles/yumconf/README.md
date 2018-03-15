# yumconf

Role which helps to manage YUM configuration.

## Examples

```
---
# Example of how to use the role
- hosts: myhost
  roles:
    - role: yumconf
      # This configuration will disable GPG checking (gpgcheck=0)
      yumconf_conf:
        main:
          cachedir: /var/cache/yum/$basearch/$releasever
          keepcache: 0
          debuglevel: 2
          logfile: /var/log/yum.log
          exactarch: 1
          obsoletes: 1
          plugins: 1
          installonly_limit: 3
          distroverpkg: "{{ ansible_distribution | lower }}-release"
          # This line will disable the GPG checking
          gpgcheck: 0
```

```
---
# Example of how to use the role
- hosts: myhost
  roles:
    - role: yumconf
      # This configuration uses an HTTP proxy (http_proxy)
      yumconf_conf:
        main:
          cachedir: /var/cache/yum/$basearch/$releasever
          keepcache: 0
          debuglevel: 2
          logfile: /var/log/yum.log
          exactarch: 1
          obsoletes: 1
          gpgcheck: 1
          plugins: 1
          installonly_limit: 3
          distroverpkg: "{{ ansible_distribution | lower }}-release"
          # This line will set up the HTTP proxy
          proxy: http://172.18.12.202:3128
```

## Role variables

List of variables used by the role:

```
# Default /etc/yum.conf configuration
yumconf_conf:
  main:
    cachedir: /var/cache/yum/$basearch/$releasever
    keepcache: 0
    debuglevel: 2
    logfile: /var/log/yum.log
    exactarch: 1
    obsoletes: 1
    gpgcheck: 1
    plugins: 1
    installonly_limit: 3
    distroverpkg: "{{ ansible_distribution | lower }}-release"
```

