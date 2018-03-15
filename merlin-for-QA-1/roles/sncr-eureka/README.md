# sncr-eureka

Role to install sncr-registry (former sncr-service-discovery) packages on a system.

## Role configuration

* eureka_version (Default: 2.0.1-0) - Eureka version to install on the setup.

## Installs the sncr-registry packages

Before it gets installed, it requires to have common and JDK on that hosts.

The following attributes are required:

* eureka_user information - defined in the 'group_vars/registry'.
* sncr_repo_url - defined in the 'group_vars/site1 | site2' file.
