# owm-cassblob

Role to install apache-cassandra blob package on a system and maintenance for it.
## Inventory file configuration

* master - For first cassandra blob node  its value will be true.This flag is used for selecting of cassandra blob master node. For other node don't need to define this flag.Same will be followed for multiple site.


## Host vars configuration
This variables needs to configured properly in host_vars/site1blob01, host_vars/site1blob02,etc for cassandra blob installation.Same will be followed for multiple site.

* Rack - For first cassandra blob node its value will be RAC1,for second cassandra blob node its value will be 
  RAC2,for thirdc cassandra blob node its value will be RAC3 etc. Same will be followed for multiple site

* cassblob_maintenance:
   - minute: "0"
     hour: "2"
     day: "*"
     month: "*"
     weekday: "*"
  (Default : configure it for 2 AM) - Defined for cron job to run at specific interval on cassandra blob node and value should be different for each node in cluster.

## Role configuration
This configurations fine tunes the cassandra in roles/owm-cassblob/defaults/main.yml file.

Change those configurations into group_vars/<groupid> or host_vars/<hostid>, only change the recommneded value as of now, other default values remain same.

* cassandra_concurrent_reads(default: 48)
* cassandra_concurrent_writes(default: 48)
* cassandra_rpc_server_type(default: hsha)
* cassandra_endpoint_snitch(default: PropertyFileSnitch)
* cassandra_num_tokens(default: 256)
* cassandra_memtable_total_space_in_mb(default: 2048)
* cassandra_start_native_transport(default: false)
* cassandra_rpc_min_threads(default :64)
* cassandra_rpc_max_threads(default: 64)
* cassandra_compaction_throughput_mb_per_sec(default: 40)
* cassandra_read_request_timeout_in_ms(default: 10000)
* cassandra_range_request_timeout_in_ms(default: 10000)
* cassandra_write_request_timeout_in_ms(default: 10000)
* cassandra_truncate_request_timeout_in_ms(default: 60000)
* cassandra_request_timeout_in_ms(default: 10000)
* cassandra_internode_compression(default: all)
* cassandra_max_heap_size(default: 2G) - For Cassandra config tunning,its recommneded value is 8G
* cassandra_heap_newsize(default: 800M) - For Cassandra config tunning,its recommneded value is 1600M
* cassandra_tombstone_failure_threshold(default: 100000)
* cassandra_batch_size_warn_threshold_in_kb(default: 5)
* cassandra_cas_contention_timeout_in_ms(deault: 1000)
* cassandra_preheat_kernel_page_cache(default: false)
* cassandra_CMSInitiatingOccupancyFraction(default: 70)


## Installs the apache-cassandra meta  package.

The following attributes are required:

* cass_user information - defined in the 'group_vars/cassandra'.
* cassandra_source_version(default:2.0.12) - defined in the 'group_vars/cassandra'.
* cass_maintenance(default: true) - defined in the 'group_vars/cassandra' and required for maintenance.

## Multi-instances deployment

It is possible to install multiple blobstore nodes on the same bare metal host.
Each instance will be listening on dedicated IP's (1 for storage/gossip, 1 for service access) and will have dedicated paths/mount points and homedirs.
The example below show how to configure the role in order to install on the same host 3 blob nodes, where

```
[site1cassandra1(bare meta host)]-ADMINVLAN:22 (management)
+- site1cassandra1-a (IPSERVICEVLAN1:9170, IPSTORAGEVLAN1:7010) data=/opt/blob1 home=/opt/cassblob1
+- site1cassandra1-a (IPSERVICEVLAN2:9170, IPSTORAGEVLAN2:7010) data=/opt/blob2 home=/opt/cassblob2
+- site1cassandra1-a (IPSERVICEVLAN3:9170, IPSTORAGEVLAN3:7010) data=/opt/blob3 home=/opt/cassblob3
```

SKIP THE ROLE 'hostname' or your host will be renamend with one of the blob instance, so please verify your command will be execute with "--skip-tag=hostname" or you will need to fix it later, e.g.
```
ansible -i <inventory> -b -m shell -a 'hostnamectl set-hostname <original_bare_metal_hostname>' <management_host>
```
Below an example of our to configure those nodes.

from the inventory:
```

# (different hostid, same ansible_ssh_host since they are all on the same host)
[site1-cassblob]
site1cassandra1-a ansible_ssh_host=10.237.224.194
site1cassandra1-b ansible_ssh_host=10.237.224.194
site1cassandra1-c ansible_ssh_host=10.237.224.194

```
from the group_vars/cassblob: 

```
# this will be used for all your blob instances.
cassandra_max_heap_size: "12G"
cassandra_heap_newsize: "2G"

# this is not required on multi-instances deployment
#
#  cass_user:
#  - username: cass
#    password: $6$vzC2PhlA$mtdUyuTmKIFP9immoEvdVof4cKgdeabEGN2QgO4BL6csiDVeht6r0wq6L7sS26CpQWw1Tf5Kv/MrZVdGNvi92.
#    name: Cassandra account 1
#    home: /opt/cass
#    groups: []
#    uid: 504
#    ssh_key: []

# multi-instances deployment accounts
cass_user1:
  - username: cassblob1
    password: $6$vzC2PhlA$mtdUyuTmKIFP9immoEvdVof4cKgdeabEGN2QgO4BL6csiDVeht6r0wq6L7sS26CpQWw1Tf5Kv/MrZVdGNvi92.
    name: Cassandra account 2
    home: /opt/cassblob1
    groups: []
    uid: 502
    ssh_key: []

cass_user2:
  - username: cassblob2
    password: $6$vzC2PhlA$mtdUyuTmKIFP9immoEvdVof4cKgdeabEGN2QgO4BL6csiDVeht6r0wq6L7sS26CpQWw1Tf5Kv/MrZVdGNvi92.
    name: Cassandra account 3
    home: /opt/cassblob2
    groups: []
    uid: 503
    ssh_key: []

cass_user3:
  - username: cassblob3
    password: $6$vzC2PhlA$mtdUyuTmKIFP9immoEvdVof4cKgdeabEGN2QgO4BL6csiDVeht6r0wq6L7sS26CpQWw1Tf5Kv/MrZVdGNvi92.
    name: Cassandra account
    home: /opt/cassblob3
    groups: []
    uid: 504
    ssh_key: []

# Support users and Cassandra user need to be created on Cassandra nodes.
# this has to be moved to the host_vars/<cassblobhost> and restricted to a single user
# cassandra_users: "{{ cass_user1 + cass_user2 + cass_user3 + support_users }}"

# tell the role we have multi-instances deployment
# 
cassandra_users: "{{ cass_user1 + cass_user2 + cass_user3 }}"
```

from the host_vars/site1cassandra1-a:

```
# which account so use for C*
cass_user_id: "cassblob1"

# tell users role the accounts required
cassandra_users: "{{ cass_user1 }}"

# paths for C*, role will check and fix ownership if required
data_file_directories: 
  - /opt/blob1/data
commitlog_directory: /opt/blob1/commitlog
saved_caches_directory: /opt/blob1/saved_caches

# nodes will be listening on 127.0.0.1, assign a different JMX port to each node
cassandra_jmx_port: "7299"
```

from the host_vars/site1cassandra1-b:

```
# which account so use for C*
cass_user_id: "cassblob2"

# tell users role the accounts required
cassandra_users: "{{ cass_user2 }}"

# paths for C*, role will check and fix ownership if required
data_file_directories: 
  - /opt/blob2/data
commitlog_directory: /opt/blob2/commitlog
saved_caches_directory: /opt/blob2/saved_caches

# nodes will be listening on 127.0.0.1, assign a different JMX port to each node
cassandra_jmx_port: "7298"
```

from the host_vars/site1cassandra1-c:

```
# which account so use for C*
cass_user_id: "cassblob3"

# tell users role the accounts required
cassandra_users: "{{ cass_user3 }}"

# paths for C*, role will check and fix ownership if required
data_file_directories: 
  - /opt/blob3/data
commitlog_directory: /opt/blob3/commitlog
saved_caches_directory: /opt/blob3/saved_caches

# nodes will be listening on 127.0.0.1, assign a different JMX port to each node
cassandra_jmx_port: "7297"
```
