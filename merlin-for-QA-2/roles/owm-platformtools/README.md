# owm-platformtools

Role to install PlatformTools package on a system.

## Role configuration

* platformtools_version (Default: 1.0.29) - The version of the PlatformTools to be installed.

## Installs the PlatformTools package

This package has a dependency on the owm-common package.

The following attributes are required:

* emailmx_user information - defined in the 'group_vars/mx'.
* owm_repo_url - defined in the 'group_vars/all' file.
* platformtools_version information - defined in the 'group_vars/mx'.

