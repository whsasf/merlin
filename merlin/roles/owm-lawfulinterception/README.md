# owm-lawfulinterception

Role to install and configure Monitoring Tool on a system.

## Role configuration

* li_home (Default: /opt/merlin/lawfulinterception) - Directory location where Monitoring Tool needs to be extracted.
* li_version (Default: 1.0.0) - Monitoring Tool version to install on the system.
* mxos_port_number (Default: 8081) - Port on which mOS is listening requests.
* callback_server_port_number (Default: 1234) - Port of the system, where Monitoring Tool is installed,
  on which Monitoring Tool will listen the notifications sent by mOS.
* jmx_remote_port (Default: 8855) - UI on which Moniroting Tool will be handled.
* monitor_storage_loc (Default: /opt/merlin/lawfulinterception/monitors) - Directory path to mount shared location, to keep monitor storage file.
* shared_loc_path - Shared location path to keep monitor storage file in <server-hostname>:<directory-location> format
* li_fstype - file system type.
