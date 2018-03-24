# owm-elk-search

Role to install Elasticsearch on a system.

## Host vars configuration
This variables needs to configured properly in host_vars/site1elk01, host_vars/site1elk02,etc for Elasticsearch nodes installation. 
It is recommended to have at least 3 master nodes (in order to avoid split brain) and 2 data nodes

* elasticsearch_data_enabled - Keep the value either "true" or "false" based on whether to save indexs on that node or not.
* elasticsearch_master_enabled - Keep the value either "true" or "false" based on the role of node for the cluster
* install_jdk_7_above - Set this variable to "true" in your host var file if you wish to install JDK version later than 7.

## Data configuration

* elasticsearch_data_path - Path to directory where to store the data (separate multiple locations by comma)

External paths for data may need to have their permissions fixed, consider to also specify for your hosts
```
required_paths:
  - /opt/data
```

## Role configuration
This configurations fine tunes the elasticsearch in "group_vars/elasticsearch" file, only change the recommended value as of now, other default values remain same.

YML_File(default: "/etc/elasticsearch")
elasticsearch_clusterName(default: "elasticcluster")- Cluster name can be any logical name.  
elasticsearch_bind_host(default: "0.0.0.0")
elasticsearch_http_port(default: "9200")
elasticsearch_http_enabled(default: "true")
