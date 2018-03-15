# owm-collectd

Role to install collectd package on a system.

## Role configuration
This configurations fine tunes the collectd in roles/owm-collectd/vars/main.yml file.

Most probably collectd gets installed on Mx components. There is no yml for this, so when installing this role, use it like following:

## Examples

```
    - hosts: directory
      roles:
        - common
		- owm-common
		- owm-mss
		- owm-collectd
```