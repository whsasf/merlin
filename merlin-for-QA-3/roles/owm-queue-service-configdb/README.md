# owm-queue-service

Role to configure configdb for the owm-queue-service deployment. It has to be executed by targeting the master configuration servers.

## Host vars configuration
This variables needs to configured properly in host_vars/site1queueservice01, host_vars/site1queueservice02,etc for queue service nodes installation.

## Role Configuration:
Variables which need to configured in vars/main.yml:

* queue_service_blob_chunk_size_in_kb: 128
* queue_service_cas_retry_count: 3
* queue_service_max_message_size_in_mb: 10
* queue_service_max_queue_length: 100000
* queue_service_max_queue_size_in_mb: 10000
* queue_service_queue_high_watermark: 90
* queue_service_queue_low_watermark: 70

* queue_service_cassmeta_read_consistency: QUORUM
* queue_service_cassmeta_write_consistency: QUORUM
* queue_service_cassblob_read_consistency: QUORUM
* queue_service_cassblob_write_consistency: QUORUM

* queue_service_cassmeta_endpoint_port: 9042
* queue_service_cassblob_endpoint_port: 9042
