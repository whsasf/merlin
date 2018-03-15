# owm-queue-service

Role to install the queue service on the system.

## Host vars configuration
This variables needs to configured properly in host_vars/site1queueservice01, host_vars/site1queueservice02,etc for queue service nodes installation.

## Role Configuration:
Variables which need to configured in vars/main.yml:

* queue_service_version(default: 1.0.0.1)