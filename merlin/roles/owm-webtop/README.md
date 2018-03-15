# WebTop

	Role to install WebTop package.

	It is assumed that IMAP, MTA, Cassandra and mOS will be installed and running before installing this package.

## Description:

	WebTop includes following components:

	* Webtop client is the presentation layer that supports standard HTML5, CSS 3, JSON and XML
	technology which allow user to access emails and address book data using major browsers on PC,
	Mac, Android and IOS devices.

	* Webtop server based on spring, java beam framework is a high performance / flexible engine
	that handle the business logic layer.

	To install WebTop, owm-common and owm-sur-common package needs to be installed and based on that it will install the necessary components for webtop.

	
## Role Configuration

	Variables which needs to configure in group_vars/uxsuite:
	
	* webtop_webmail_name (default: kiwi-octane) - Name of WebTop product
	
	Variables which needs to configure in vars/main.yml:

	* webtop_tomcat_version (default: 7.0.52-6) - Version of WebTop tomcat package
	* rpmforge_release_version (default: 0.5.3-1) - Version of rpmforge package
	* apache_openoffice_version (default: 4.1.0) - Version of apache open office
	* webtop_media_version (default: 1.0.6-1) - Version for webtop media
	* webtop_webmail_version (default: 2.0.35-0) - Version of WebTop product

	After successful installation of above role, you can check home login page of webtop by hitting this URL:
	For Desktop (Rich UI): http://<WebTop-hostname>:<WebTop-tomcat-configured-port(default is 8080)>/<webtop_product_name>/index-rui.jsp
	For Mobile device(Touch UI)://<WebTop-hostname>:<WebTop-tomcat-configured-port(default is 8080)>/<webtop_product_name>/index-tui.jsp
	
	An example: http://172.20.0.8:8080/kiwi-octane/index-rui.jsp

