# owm-system-validation

Role to get setup information.
Setup information contains:
* General information like, process related data, physical disk space, etc.
* Information about specific components(Mx, Cassandra, mOS)
* Versions of components, number of components, say the setup might have 2 mOS, it will show their information.

## Role configuration

* tomcat_server_version (Default: 7.0.61) - tomcat server version present at the central repository.
* tomcat_server_install_dir (Default: /opt/merlin) - path to install tomcat on the specified host.
* tomcat_server_pid_file (Default: /opt/merlin/bin/.pid) - sets the environment variable CATALINA_PID on the system.
* tomcat_server_http_port (Default: 8080) - set the http port for tomcat server.

## Attributes required

* emailmx_user information - defined in the 'group_vars/mx'.
* owm_tar_url - defined in the 'group_vars/all' file.
* conf_server_ipaddress - defined in the inventory file. It can be accessed by ansible variable.
* tomcat_server_ipaddress - defined in the inventory file. It can be accessed by ansible variable.
* path of 'webapps' directory inside the tomcat server
