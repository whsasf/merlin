# owm-nginx-ha

Role to install Affinity manager and it's components that include pacemaker and corosync.

## Host vars configuration

Following variables needs to configured properly in host_vars/site1afnmss01 file. where site1afnmss01 is host file for affinity manager for mss for cluster 01 in site1

* clusterId: cluster01 - Cluster id
* VIP: 172.20.0.200 - VIP for mss

same variables we need to configured for affinity manager host file for mos.


## Role configuration

Following variables needs to be configured

* owm_nginx_version - nginx version defined in  group_vars/affinity
* mos_listening_port - mos Server listening port defined in  group_vars/affinity
* mss_listening_port - mss listening port defined in  group_vars/affinity
* owm_repo_url - defined in the 'group_vars/all' file.
