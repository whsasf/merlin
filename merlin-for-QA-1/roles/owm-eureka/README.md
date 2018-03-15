# owm-eureka

Role to install owm-service-discovery packages on a system.

## Role configuration

* eureka_version (Default: 1.0.3-1.noarch) - Eureka version to install on the setup.

## Installs the owm-service-discovery packages

Before it gets installed, it requires to have common and JDK on that hosts.

The following attributes are required:

* eureka_user information - defined in the 'group_vars/directory'.
* eureka_version information - defined in the 'group_vars/directory'.
* owm_repo_url - defined in the 'group_vars/all' file.
