# owm-logstash-shipper
	
Role to install logstash shipper
	
## Description
    
Logstash allows you to pipeline data to and from anywhere. This is called an ETL (for Extract, Transform, Load) pipeline in the Business Intelligence and Data warehousing world, and it is what allows us to fetch, transform, and store events into ElasticSearch.
Logsatshshipper reads logs from all component's system and send logs into redis. 
    	
## Role Configuration
   
Variable need to configure in vars/main.yml:

* logstash_main_version and logstash_sub_version - If logstash version you wish to install is 1.5.4 then set logstash_main_version : 1.5 and logstash_sub_version : 4

* appsuite_log_path: /var/log  - Location of Appsuite log file.
* mysqld_log_path: /var/log    - Location of mysql log file.
* nagios_log_path: /var/log    - Location of Nagios log file.
* python_script_path: /var/log - Location of Python log file.
* scality_log_path: /var/log   - Location of Scality log file.

Most probably logstash-shipper gets installed on components who have log files. There is no yml for this, so when installing this role, use it like following:

## Examples

```
    - hosts: directory
      roles:
        - common
		- owm-common
		- owm-mss
		- owm-logstash-shipper
```