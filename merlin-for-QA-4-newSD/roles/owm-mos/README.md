# owm-mos

Role to install owm-mos packages on a system.

## Role configuration

* mos_version (Default: 2.4.0-3) - mOS version to install on the setup.
* mos_third_party_version (Default: 2.4.0) - mOS third party version required to install.

## Installs the owm-mos packages

Before it gets installed, it requires to have owm-mx-common on that hosts.

The following attributes are required:


* emailmx_user information - defined in the 'group_vars/mx'.
* mos_version information - defined in the 'group_vars/directory'.
* mos_third_party_version information - defined in the 'group_vars/directory'.
* owm_repo_url - defined in the 'group_vars/all' file.
