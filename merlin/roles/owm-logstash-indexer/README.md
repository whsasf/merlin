# owm-logstash-indexer
	
Role to install logstashindexer
	
## Description
    
Logstash allows you to pipeline data to and from anywhere. This is called an ETL (for Extract, Transform, Load) pipeline in the Business Intelligence and Data warehousing world, and it is what allows us to fetch, transform, and store events into ElasticSearch.
Logsatshindexer reads logs redis and parse logs using grok pattern for appropriate system type. 
    	
## Role Configuration

Variable need to configure in vars/main.yml:   

* logstash_main_version and logstash_sub_version - If logstash version you wish to install is 1.5.4 then set logstash_main_version : 1.5 and logstash_sub_version : 4

PLEASE CONFIGURE BELOW EMAIL ALERT RELATED VARAIBLES PROPERLY, ELSE IT WILL CAUSE LOGSTASH INDEXER TO CRASH!!

SET_EMAIL_ALERT (default: "false") - Set this to "true" if wish to receive email alert for error types of logs.
mailfrom (default: testemail@owmessaging.com) - Sender's email ID
mailto (default: testemail@owmessaging.com) - Receiver's email ID
mailfrom_password (default: P@ssw0rd) - Sender's email password
email_alert_params (default: ["Erro", "ERROR"] ) - Severity names to configure for email alert
smtpporthost (default: smtp.office365.com) - Host for SMTP server of your email service.
smtpport (default: 587) - Port for SMTP server of your email service.
maildomain (default: smtp.office365.com) - Mail domain for SMTP server of your email service.