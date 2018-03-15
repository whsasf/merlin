# owm-nmap

Role to install  & configure NMAP Security tool. Also it scnas all the hosts in the setup and generates the report.
Nmap: used to discover hosts and services on a computer network
features include:
 
* Host discovery – Identifying hosts on a network. For example, listing the hosts that respond to TCP and/or ICMP requests or 
  have a particular port open.
* Port scanning – Enumerating the open ports on target hosts.
* Version detection – Interrogating network services on remote devices to determine application name and version number.[6]
* OS detection – Determining the operating system and hardware characteristics of network devices.

## Role configuration

* nmap_report_file_name (Default: /opt/merlin/nmap/nmap_report) - absolute path where the report will be downloaded. 
  NMAP will generate the report in three formats: gnmap, nmap, and xml.
