# owm-nessus-server

Role to install Nessus Security tool.
Nessus allows scans for the following types of vulnerabilities:

* Vulnerabilities that allow a remote hacker to control or access sensitive data on a system.
* Misconfiguration (e.g. open mail relay, missing patches, etc.).
* Denials of service against the TCP/IP stack by using malformed packets

## Role configuration

* nessus_activation_code - activation code required to register and activate the nessus server.
  NOTE: the activation code will active Nessus for only 15 days. The same activation code can not be used again once Nessus 
  is activated.
* owm_nessus_username - to login to the nessus server. Defined in the 'group_vars/all' file.
* owm_nessus_password - to login to the nessus server. Defined in the 'group_vars/all' file.


## Attributes required

* owm_repo_url - defined in the 'group_vars/all' file.
