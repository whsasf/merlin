# owm-kibana

Role to install Kibana component

## Description

Kibana is an open source data visualization platform that allows you to interact with your data through stunning, powerful graphics that can be combined into custom dashboards.

Variables that needs to be configured:

	* kibana_dir (default: /opt/kibana) - Directory in which Kibana will get installed
	* kibana_version (default: 4.1.1) - Version of kibana
	* kibana_port (default: 5601) - Kibana port
	* kibana_host (default: 0.0.0.0) - Kibana address to bind to.
	* elasticsearch_preserve_host (default: "true") - Elasticsearch preserve host
	* default_kibana_index (default: .kibana) - Kibana index
	* default_app_id (default: discover) - Default app id
	* request_timeout (default: 300000) - Timeout for request
	* shard_timeout (default: 0) - Timeout for Shard
	* verify_ssl (default: "true") - Var for whether ssl verify should be true or not