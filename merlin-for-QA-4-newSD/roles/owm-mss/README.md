# owm-mss

Role to install owm-msg-mss packages on a system and for mss maintenance.

## Host vars configuration

This variables needs to configured properly host_vars/site1mss01 etc for mss maintenance.

* mss_maintenance:
   - minute: "0"
     hour: "1
     day: "*"
     month: "*"
     weekday: "*"
    (default: Configure it for 1 AM) - defined for cron job to run at specific interval on cassandra meta node

## Role configuration

* blobstore_cluster_port (default: 9162) - port on which cassandra blob server is listening.
* metadata_cluster_port (default: 9161) - port on which cassandra meta server is listening.
* duration(default:3600) - Duration in seconds for mss maintenance

## Installs the owm-mss packages

The following attributes are required:

* conf_server_name - hostname of the server where conf-server is installed. It is taken by the Ansible Playbook.
* emailmx_user information - defined in the 'group_vars/mx'.
* emailmx_version - defined in the 'group_vars/mx' file.
* owm_repo_url - defined in the 'group_vars/all' file.
* cluster_name - mss cluster name. It can have any value.
* metadata_cluster_host - hostnames/ip-addresses of the machines where cassandra meta is installed. It is taken by the Ansible Playbook.
* blobstore_cluster_host - hostnames/ip-addresses of the machines where cassandra blob is installed. It is taken by the Ansible Playbook.
* meta_cluster_name: metacluster - CassandraMDCluster defined in the 'group_vars/all' required for mss maintenance.
* mx_maintenance:(default: true) - Defined in 'group_vars/mx' and It is required for maintenance.
