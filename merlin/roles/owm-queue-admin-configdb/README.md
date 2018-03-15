# owm-queue-admin

Role to configure configdb for the owm-queue-admin deployment. It has to be executed by targeting the master configuration servers.

## Host vars configuration
This variables needs to configured properly in host_vars/site1qadminsearch01, host_vars/site1qadminsearch02,etc for qadminsearch nodes installation.

## Role Configuration:
Variables which need to configured in vars/main.yml:

* queue_admin_cassmeta_read_consistency: QUORUM
* queue_admin_cassmeta_write_consistency: QUORUM
* queue_admin_cassblob_read_consistency: QUORUM
* queue_admin_cassblob_write_consistency: QUORUM

* cassandra_meta_native_transport_port: 9042
* cassandra_blob_native_transport_port: 9042