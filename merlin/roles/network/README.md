network
=================

This role enables users to configure various network components on target
machines. The role can be used to configure:

- Ethernet interfaces
- Network routes

Examples
--------

Configure eth1 and eth2 on a host with a static IP and a DHCP IP. Also
define static routes and a gateway.

```
    - hosts: myhost
      roles:
        - role: network
          ethernet_interfaces:
           - device: eth1
             bootproto: static
             address: 192.168.10.18
             netmask: 255.255.255.0
             gateway: 192.168.10.1
             route:
              - network: 192.168.200.0
                netmask: 255.255.255.0
                gateway: 192.168.10.1
              - network: 192.168.100.0
                netmask: 255.255.255.0
                gateway: 192.168.10.1
           - device: eth2
             bootproto: dhcp
```

