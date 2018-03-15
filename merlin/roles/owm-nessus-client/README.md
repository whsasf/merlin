# owm-nessus-client

Role to create scans on Nessus Security tool.
This role executes various CURL REST APIs to create scan, launch scan and download the report of the scan for the setup.

## Role configuration

* initilize_time (Default: 20 minutes) - time to initilize the Nessus Server.
* nessus_report_format (Default: csv) - format of the generated report, it can be 'csv' or 'html'.
* nessus_report_download_location (Default: /opt/merlin/nessus) - download the report at the specified location.
* scan_name (Default: owmScan) - Any String value.
* scan_description (Default: SetupScan) - Description about the scan.
* scan_completion_time (Default: 180 minutes) - wait time to complete the scan.

