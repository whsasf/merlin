# merlin-QA
###**Changes in this version : merlin-for-QA-3**
1. take "common" and "jdk" rols out from each yml file. take "user" role out from common role .
2. add restart mx role to solve issues happened after mx upgrading.



###**Changes in this version : merlin-for-QA-2**
**1. split integrated playbooks into independent ones , as below :**

  	 #- include: bootstrap.yml
 	 #- include: initssh.yml --ask-pass
  	- include: cassmeta.yml
	- include: cassblob.yml
	- include: eureka.yml
	- include: confserv.yml
	- include: dirserv.yml
	- include: dircacheserv.yml
	- include: mxos.yml
  	- include: mss.yml
	- include: imap.yml
	- include: pop.yml
	- include: mta.yml
	- include: queue.yml
	- include: extserv.yml
	- include: qadmin.yml
	- include: elasticsearch.yml
	- include: qsearch.yml
	- include: qservice.yml
	- include: pab.yml
	- include: cal.yml
	- include: search.yml
	- include: platformtools.yml 
		  
**2.  fixed all the known issues after installation in previous version(basically you don't have to do any repairing work after installtion this time ), which are:**
    
    (1)platformtools path lost issue;
    (2)ports_offsets doesn't work issue;now the default ports_offset is 20000, you can change it in group_vars/all .
    (3)empty values of mxos keys that relating to mss,pab,cal ;
    (4)mxos maxthreads default value changing to 2000 ;
    (5)change default mxos.log type to INFO;
    (6) change mxos "hazelcast" multicast to false by default ;
    (7)elacticsearch can not run issue. Please note: if you need esastic search ,2 nodes are suggested, because 1 elasticsearch may not running properly sometimes.
    (8)each component installing will only create the user account that managing this component.
    (9)Apply the accounts limits to "*" (all users) to avoid specific account limits been overwriten.
    (10)Replace the old service-discovery version to new one  ,named sncr-registry. 
    (11)search server does not work issue;
    (12) reduce the pause time to save total installtion time
    (13)correct 1 error in confserv role during upgrade. 
    (14)solved the mta and msg-queue "immtacheck" error during update
    (15) add "--request-timeout =60 " solve cqlsh import schema timeout issue  
    
    
**3.  the new merlin-qa package location:**
scp op-user@10.49.58.239:/opt/ansible/merlin/merlin-for-QA-2.zip    .  
password:letmein

PS: if you really need the old version service-discovery ,the merlin with this package also available with all fixed above:  merlin-for-QA-1.zip
**4.  the backup location for repo:**
owm_repo_url: http://10.49.58.243/repo/rpms
owm_tar_url: http://10.49.58.243/repo/tarfiles

