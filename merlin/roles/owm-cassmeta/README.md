# owm-cassmeta

Role to install apache-cassandra meta package on a system and maintenance for it.
## Inventory file configuration

* master - For first cassandra meta node  its value will be true.This flag is used for selecting of cassandra meta master node. For other node don't need to define this flag.Same will be followed for multiple sites.

## Host vars configuration
This variables needs to configured properly in host_vars/site1met01, host_vars/site1met02,etc for cassandra meta installation. Same will be followed for multiple site.

* cassandra_rack - For first cassandra meta node its value will be RAC1,for second cassandra meta node its value
 will be RAC2 ,for third cassandra meta node its value will be RAC3 etc. Same will be followed for multiple site

* cassmeta_maintenance:
   - minute: "0"
     hour: "2"
     day: "*"
     month: "*"
     weekday: "*"
  (default: Configure it for 2 AM) - defined for cron job to run at specific interval on cassandra meta node and value should be different for each node in cluster.

## Role configuration
This configurations fine tunes the cassandra in roles/owm-cassmeta/defaults/main.yml file.

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

* cassandra_source_version(default:2.0.12) - defined in the 'group_vars/cassandra'. 
* cass_user information - defined in the 'group_vars/cassandra'.
* cass_maintenance(default: true) - defined in the 'group_vars/cassandra' and required for maintenance.


