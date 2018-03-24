# owm-mss-configdb

Role to perform update on configdb for mss and imboxmaint. It has to be executed after the owm-mss role by targeting the directory groups (where the primary config server is deployed).
Based on the CSC/platform, imboxmaint has to be configured in order to:
- Split groups for maintenance
- Assign clusterName into the configdb

## configuration keys

- maintenance_group_number: 200 - the number of groups / mss

- mx_mailboxaging: false - enable/disable mailboxaging configuration
- mailbox_aging_enabled: 'false' - enable mailboxaging (if mx_mailboxaging is true)
- mailbox_aging_max_age_days: 10 - max age (days) in order to add inactive mailbox having lastAccess older then 10 days to CF_MailboxAged 


