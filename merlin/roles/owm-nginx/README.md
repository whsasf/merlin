# owm-nginx

Role to install owm-nginx package on a system.

## Role configuration

* clusterId - defined in the 'host_vars' file of specific host. The value can be 01, 02, etc.
* component - defined in the 'host_vars' file of specifi host. The value can be 'mss', 'mos', 'failover, etc.

If anyone wants to re-use this role, follow the below steps:

 1. The inventory file should have the below group defined as:
    Example:
    [site1-affinity-mss]
    site1afnmss01
 
 2. Now, create a 'host_vars' file as site1afnmss01, it should have the following variables:
    Example:
    clusterId: cluster01
    component: mss

 3. Put the nginx.conf file specific to the component in 'owm-nginx/templates' directory.
    Example:
    nginx_mss.conf

 4. Change the 'main.yml' file from the 'owm-nginx/tasks' directory to execute the NGINX for the specified component.
    Example:
    - name: Determine the node component
      set_fact:
        node_component: "['mss']"
      when: component == "mss"
      tags: [ 'owm-affinity','owm-nginx' ]
 
This role can be added as given below:

Example:

    ---
    - hosts: affinity
      roles:
        - common
        - owm-nginx
        - owm-aginx-ha

