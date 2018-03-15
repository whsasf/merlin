import threading
import paramiko
import os
import subprocess
import sys
import re
import time
from datetime import datetime

single_line_formatting = lambda data: data.replace("\n","<br>")

user_dir_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
full_path = user_dir_path + "/.ssh/id_rsa"
max_number_of_lines = 0
def get_output_format(res,cmd):
	"""This Function formats output"""
	output_list = []
	for line in res:
		line = line.replace("\n","<br>")
		line = line.replace(" ","&nbsp;")
		line = line.replace("\t","&nbsp;&nbsp;&nbsp;")
		output_list.append('<font size="2" color="grey">'+line+'</font>')
	return output_list

def get_ouput_format_with_heading(res, cmd):
	"""This Function formats output"""
	extra_tabs = ['disk_size','spool_dir_data','mounted_devices_data','lsof_list']
	output_list = []
	counter = 0
	for line in res:
		line = line.replace("\n","<br>")
		if cmd in extra_tabs:
			line = line.replace("\t","&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
		else:
			line = line.replace("\t","&nbsp;&nbsp;&nbsp;")
		line = line.replace(" ","&nbsp;")
		if counter == 0:
			output_list.append('<font size="2" color="black"><b>'+line+'</b></font>')
		else:
			output_list.append('<font size="2" color="grey">'+line+'</font>')
		counter+=1
		if counter > max_number_of_lines:
			break
	return output_list

def get_ouput_format_with_splitdata(res, cmd):
	"""This Function formats output"""
	output_list = []
	for line in res:
		line = line.replace("\n","<br>")
		line = line.replace(" ","&nbsp;")
		line = line.replace("\t","&nbsp;&nbsp;&nbsp;")
		if cmd != 'sysctldata':
			version_split = line.split(":")
			if len(version_split) == 2:
				if cmd  == 'mem_info' or cmd == 'se_status':
					output_list.append('<font size="2" color="black"><b>'+version_split[0]+'&nbsp;&nbsp;:</b></font><font size="2" color="grey">'+version_split[1])
				else:
					output_list.append('<font size="2" color="black"><b>'+version_split[0]+'&nbsp;&nbsp;:&nbsp;</b></font><font size="2" color="grey">'+version_split[1])
		
		elif cmd == 'sysctldata':
			version_split = line.split("=")
			if len(version_split) == 2:
				output_list.append('<font size="2" color="black"><b>'+version_split[0]+'&nbsp;&nbsp;=</b></font><font size="2" color="grey">'+version_split[1])
	
	return output_list

def command_exc(conn_obj,cmd,cmd_key):
	res_data = []
	stdin, stdout, stderr =  conn_obj.exec_command(cmd)
	res = stdout.readlines()
	if res:
		res_data+=get_output_format(res, cmd_key)
	elif not res:
		if cmd_key == 'telnet_stat':
			res_data.append('<font size="2" color="#FA5858"> Telnet Not Running !!!</font>')
		elif cmd_key == 'ftp_stat':
			res_data.append('<font size="2" color="#FA5858"> FTP Not Running !!!</font>')
		elif cmd_key == 'rlogin_stat':
			res_data.append('<font size="2" color="#FA5858"> rLogin Not Running !!!</font>')
		else:
			res_data.append('<font size="2" color="#FA5858"> Data Not Found !!!</font>')
	#print "RES DATA Is &&&&&&&&&*********", res_data
	return res_data

def command_exc_2(conn_obj,cmd,cmd_key):
	res_data = []
	stdin, stdout, stderr =  conn_obj.exec_command(cmd)
	res = stdout.readlines()
	if res:
		res_data+=get_ouput_format_with_heading(res, cmd_key)
	elif not res:
		res_data.append('<font size="2" color="#FA5858"> Data Not Found !!!</font>')
	return res_data
	
def command_exc_3(conn_obj,cmd,cmd_key):
	res_data = []
	stdin, stdout, stderr =  conn_obj.exec_command(cmd)
	res = stdout.readlines()
	if res:
		res_data+=get_ouput_format_with_splitdata(res, cmd_key)
	elif not res:
		res_data.append('<font size="2" color="#FA5858"> Data Not Found !!!</font>')
	return res_data

	
	
def mx_comp_version(host_ip,process_key,profile_username,profile_password,ansible):
	"""mx_comp_version Function is triggered on Ansible and Standalone mode.
	   This Function connects to MX machine and finds out MX Version"""
	sys_data_dict = {}
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	paramiko.util.log_to_file("python_connect.log")
	try:
		if ansible==False:
			ssh.connect(host_ip, username=profile_username,password=profile_password)
		if ansible==True:
			ssh.connect(host_ip, username='root', key_filename=full_path)
		cmd = "rpm -qa| grep "+process_key+"-"
		sys_data_dict.update({'mx_version':command_exc(ssh,cmd,'version')})
		return sys_data_dict
	except:
		print "Exception found"
		print sys.exc_info()[0] , "mx_comp_version For Host ", host_ip
	ssh.close()
	
def get_cassandra_data(host_ip,profile_username,profile_password,path,meta_blob_check,ansible):
	"""get_cassandra_data Function is triggered on Ansible and Standalone mode.
	   This Function connects to Cassandra Meta and Blob machines and finds out Cassandra Version and Cassandra Ring structure"""
	sys_data_dict = {}
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	paramiko.util.log_to_file("python_connect.log")
	try:
		if ansible==False:
			ssh.connect(host_ip, username=profile_username,password=profile_password)
		if ansible==True:
			ssh.connect(host_ip, username='root', key_filename=full_path)
		stdin, stdout, stderr =  ssh.exec_command('find '+path+' -name nodetool')
		nodetool_path = stdout.readlines()
		if nodetool_path:
			for line in nodetool_path:
				proper_path = re.findall(meta_blob_check, line)
				if proper_path:
					line = line.rstrip('\r\n')
					stdin, stdout, stderr =  ssh.exec_command(line+' -h localhost version')
					cass_version = stdout.read()
					if not cass_version:
						cass_version = "Data Not Found !!!"
						cass_version = '<font size="2" color="#FA5858">'+cass_version+'</font>'
					else:
						cass_version = '<font size="2" color="grey">'+cass_version+'</font>'
					cass_version = single_line_formatting(cass_version)
					sys_data_dict.update({'cassandra_version':cass_version})
					
					stdin, stdout, stderr =  ssh.exec_command(line.rstrip('\r\n')+' -h localhost status')
					cass_status = stdout.read()
					if not cass_status:
						cass_status = "Data Not Found !!!"
						cass_status = '<font size="2" color="#FA5858">'+cass_status+'</font>'
					else:
						cass_status = '<font size="2" color="grey">'+cass_status+'</font>'
					cass_status = single_line_formatting(cass_status)
					sys_data_dict.update({'cassandra_ring_status':cass_status})
				
		else:
			stdin, stdout, stderr =  ssh.exec_command('. .profile;nodetool -h localhost version')
			cass_version = stdout.read()
			if not cass_version:
				cass_version = "Data Not Found !!!"
				cass_version = '<font size="2" color="#FA5858">'+cass_version+'</font>'
			else:
				cass_version = '<font size="2" color="grey">'+cass_version+'</font>'
			cass_version = single_line_formatting(cass_version)
			sys_data_dict.update({'cassandra_version':cass_version})
			
			stdin, stdout, stderr =  ssh.exec_command('. .profile;nodetool -h localhost ring')
			cass_status = stdout.read()
			if not cass_status:
				cass_status = "Data Not Found !!!"
				cass_status = '<font size="2" color="#FA5858">'+cass_status+'</font>'
			else:
				cass_status = '<font size="2" color="grey">'+cass_status+'</font>'
			cass_status = single_line_formatting(cass_status)
			sys_data_dict.update({'cassandra_ring_status':cass_status})
		
		return sys_data_dict
	except:
		print "Exception found"
		print sys.exc_info(), " For Host ", host_ip
	ssh.close()
	
def profile_data(host_ip,profile_username,profile_password,ansible,path):
	"""profile_data Function is triggered on Ansible and Standalone mode.
	   This Function connects to each component's machines and finds out .profile Data"""
	sys_data_dict = {}
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	paramiko.util.log_to_file("python_connect.log")
	try:
		if ansible==False:
			ssh.connect(host_ip, username=profile_username,password=profile_password)
			cmd = 'cat .profile'
		elif ansible==True:
			ssh.connect(host_ip, username='root', key_filename=full_path)
			cmd = 'cd '+path+';cat .profile'
		sys_data_dict.update({'profile_data':command_exc(ssh,cmd,'profile_data')})
		
		return sys_data_dict
	except:
		print "Exception found"
		print sys.exc_info() , ".Profile data For Host ", host_ip
	ssh.close()
	
def spool_dir_check(host_ip,username,password,dir_path,ansible):
	"""spool_dir_check Function is triggered on Ansible and Standalone mode.
	   This Function connects to each of MX component's machines and finds out Spool Directory Structure"""
	sys_data_dict = {}
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	paramiko.util.log_to_file("python_connect.log")
	try:
		if ansible==False:
			ssh.connect(host_ip, username=username,password=password)
		if ansible==True:
			ssh.connect(host_ip, username='root', key_filename=full_path)
		cmd = 'df -h '+dir_path
		sys_data_dict.update({'spool_dir_data':command_exc_2(ssh,cmd,'spool_dir_data')})
		return sys_data_dict
	except:
		print "Exception found"
		print sys.exc_info(), " For Host ", host_ip
	ssh.close()
	
	
def get_server_info(host_ip,server_username,server_password,process_name,ansible):
	"""get_server_info Function is triggered on Ansible and Standalone mode.
	   This Function connects to each component's machines and Run's series of Generic Commands"""
	sys_data_dict = {}
	paramiko.util.log_to_file("python_connect.log")
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		if ansible==False:
			ssh.connect(host_ip, username=server_username,password=server_password)
		elif ansible==True:
			ssh.connect(host_ip, username='root', key_filename=full_path)
			
		cmd_running_mods_list = 'lsmod'
		sys_data_dict.update({'running_mod_info':command_exc_2(ssh,cmd_running_mods_list,'running_mods_list')})
		
		cmd_cifsiostat = 'cifsiostat'
		sys_data_dict.update({'cifsiostat_data':command_exc(ssh,cmd_cifsiostat,'cifsiostat_data')})
	
		cmd_nfsiostat = 'nfsiostat'
		sys_data_dict.update({'nfsiostat_data':command_exc(ssh,cmd_nfsiostat,'nfsiostat_data')})
		
		cmd_nestat = 'netstat'
		sys_data_dict.update({'netstat_data':command_exc(ssh,cmd_nestat,'netstat_data')})
		
		cmd_dmidecode = 'dmidecode -t 17'
		sys_data_dict.update({'dmidecode_data':command_exc(ssh,cmd_dmidecode,'dmidecode_data')})
		
		cmd_disk_size = 'df -h'
		sys_data_dict.update({'disk_size':command_exc_2(ssh,cmd_disk_size,'disk_size')})
		
		cmd_no_of_disks = 'lsblk'
		sys_data_dict.update({'no_of_disks':command_exc_2(ssh,cmd_no_of_disks,'no_of_disks')})

		cmd_proc_status = "ps -A"
		sys_data_dict.update({'process_status':command_exc_2(ssh,cmd_proc_status,'proc_status')})

		cmd_ss_data = "ss -l"
		sys_data_dict.update({'ss_data':command_exc_2(ssh,cmd_ss_data,'ss_data')})

		cmd_mounted_device_data = 'df -aTh'
		sys_data_dict.update({'mounted_devices_data':command_exc_2(ssh,cmd_mounted_device_data,'mounted_devices_data')})

		cmd_lsof_list = 'lsof'
		sys_data_dict.update({'lsof_list':command_exc_2(ssh,cmd_lsof_list,'lsof_list')})
		
		cmd_cpu_info = 'cat /proc/cpuinfo'
		sys_data_dict.update({'cpu_info':command_exc_3(ssh,cmd_cpu_info,'cpuinfo')})
		
		stdin, stdout, stderr =  ssh.exec_command("lsb_release -i -r")
		rhel_version = []
		res = stdout.readlines()
		# print "rhel_version**** Outside", res
		if res:
			rhel_version+=get_ouput_format_with_splitdata(res, 'rhel_version')
		elif not res:
			stdin, stdout, stderr =  ssh.exec_command("cat /etc/redhat-release")
			result = stdout.readlines()
			# print "rhel_version**** Inside", result
			if result:
				rhel_version+=get_output_format(result, 'rhel_version')
			elif not result:
				rhel_version.append('<font size="2" color="#FA5858"> Data Not Found !!!</font>')
		sys_data_dict.update({'rhel_version_info':rhel_version})
		
		cmd_mem_info = 'cat /proc/meminfo'
		sys_data_dict.update({'memory_info':command_exc_3(ssh,cmd_mem_info,'mem_info')})
		
		cmd_se_status = "sestatus"
		sys_data_dict.update({'SeLinux_status':command_exc_3(ssh,cmd_se_status,'se_status')})
		
		cmd_sysctldata = "sysctl -a"
		sys_data_dict.update({'sysctl_data':command_exc_3(ssh,cmd_sysctldata,'sysctldata')})
		
		cmd_rpm_list = "rpm -qa"
		sys_data_dict.update({'rpm_list_info':command_exc(ssh,cmd_rpm_list,'rpm_list')})
		
		cmd_ntp_ver = "rpm -qa| grep ntp"
		sys_data_dict.update({'ntp_version':command_exc(ssh,cmd_ntp_ver,'ntp_version')})
		
		cmd_chkconfig = "chkconfig --list"
		sys_data_dict.update({'chkconfig_enabled_services':command_exc(ssh,cmd_chkconfig,'chkconfig')})
		
		cmd_ssh_stat = "ps aux | grep sshd | grep -v grep"
		sys_data_dict.update({'ssh_status':command_exc(ssh,cmd_ssh_stat,'ssh_stat')})
		
		cmd_telnet_stat = "ps aux | grep telnet | grep -v grep"
		sys_data_dict.update({'telnet_status':command_exc(ssh,cmd_telnet_stat,'telnet_stat')})
		
		cmd_ftp_stat = "ps aux | grep vsftpd | grep -v grep"
		sys_data_dict.update({'ftp_status':command_exc(ssh,cmd_ftp_stat,'ftp_stat')})
		
		cmd_rlogin_stat = "ps -ef |grep inetd"
		sys_data_dict.update({'rlogin_status':command_exc(ssh,cmd_rlogin_stat,'rlogin_stat')})
		
		cmd_sar_data = "sar"
		sys_data_dict.update({'sar_data':command_exc(ssh,cmd_sar_data,'sar_data')})
		
		cmd_iostat = "iostat"
		sys_data_dict.update({'iostat_data':command_exc(ssh,cmd_iostat,'iostat_data')})
		
		cmd_mpstat = "mpstat"
		sys_data_dict.update({'mpstat_data':command_exc(ssh,cmd_mpstat,'mpstat_data')})
		
		cmd_vmstat = "vmstat"
		sys_data_dict.update({'vmstat_data':command_exc(ssh,cmd_vmstat,'vmstat_data')})
		
		cmd_free = "free"
		sys_data_dict.update({'free_mem_data':command_exc(ssh,cmd_free,'free_mem_data')})
		
		cmd_w = "w"
		sys_data_dict.update({'w_data':command_exc(ssh,cmd_w,'w_data')})

		cmd_iwconfig = 'iwconfig'
		sys_data_dict.update({'interface_data':command_exc(ssh,cmd_iwconfig,'interface_data')})
		
		cmd_list_users = 'cat /etc/passwd | cut -d: -f1'
		sys_data_dict.update({'list_users':command_exc(ssh,cmd_list_users,'list_users')})
		
		cmd_system_users = "awk -F':' -v 'min=500' -v 'max=60000' '{ if ( $3 >= min ) print $0}' /etc/passwd"
		sys_data_dict.update({'system_users':command_exc(ssh,cmd_system_users,'system_users')})
		
		cmd_list_groups = 'cat /etc/group |cut -d: -f1'
		sys_data_dict.update({'list_groups':command_exc(ssh,cmd_list_groups,'list_groups')})
		
		cmd_admin_users = "grep '[^:]*:[^:]*:0:' /etc/passwd"
		sys_data_dict.update({'admin_users':command_exc(ssh,cmd_admin_users,'admin_users')})
		
		cmd_getent_data = 'getent group root wheel adm admin'
		sys_data_dict.update({'getent_data':command_exc(ssh,cmd_getent_data,'getent_data')})
		
		# Keeping below commands as we may need to add them in future.
		
		# stdin, stdout, stderr =  ssh.exec_command('openssl s_client -no_ssl2 -ssl3 -no_tls1 -host 127.0.0.1 -port 443')
		# ssl_protocol = []
		# res =stdout.readlines()
		# if res:
		# 	ssl_protocol+=get_output_format(res,'ssl_protocol')
		# elif not res:
		#	ssl_protocol.append('<font size="2" color="#FA5858"> Data Not Found !!!</font>')
		# sys_data_dict.update({'ssl_protocol':ssl_protocol})
		
		# stdin, stdout, stderr =  ssh.exec_command('openssl s_client -cipher LOW:EXP -port 443 -host 127.0.0.1')
		# ssl_cipher = []
		# res =stdout.readlines()
		# if res:
		# 	ssl_cipher+=get_output_format(res,'ssl_cipher')
		# elif not res:
		#	ssl_cipher.append('<font size="2" color="#FA5858"> Data Not Found !!!</font>')
		# sys_data_dict.update({'ssl_cipher':ssl_cipher})
		
		# stdin, stdout, stderr =  ssh.exec_command('cat /etc/httpd/conf/httpd.conf | grep -w  ServerTokens')
		# http_server_sign = []
		# res =stdout.readlines()
		# if res:
		# 	http_server_sign+=get_output_format(res,'http_server_sign')
		# elif not res:
		#	http_server_sign.append('<font size="2" color="#FA5858"> Data Not Found !!!</font>')
		# sys_data_dict.update({'http_server_sign':http_server_sign})
		
		# stdin, stdout, stderr =  ssh.exec_command('cat /etc/httpd/conf/httpd.conf | grep -w  HostnameLookups')
		# hostname_lookup = []
		# res =stdout.readlines()
		# if res:
		# 	hostname_lookup+=get_output_format(res,'hostname_lookup')
		# elif not res:
		#	hostname_lookup.append('<font size="2" color="#FA5858"> Data Not Found !!!</font>')
		# sys_data_dict.update({'hostname_lookup':hostname_lookup})
		
		# stdin, stdout, stderr =  ssh.exec_command('cat /etc/httpd/conf/httpd.conf | grep -w  "LimitExcept"')
		# http_methods = []
		# res =stdout.readlines()
		# if res:
		# 	http_methods+=get_output_format(res,'http_methods')
		# elif not res:
		#	http_methods.append('<font size="2" color="#FA5858"> Data Not Found !!!</font>')
		# sys_data_dict.update({'http_methods':http_methods})
		
		cmd_nic_card = 'ifconfig -a'
		sys_data_dict.update({'nic_card_data':command_exc(ssh,cmd_nic_card,'nic_card_data')})
		
		if process_name == 'MXOS':			
			cmd_mxos_ver = "rpm -qa | grep mxos"
			sys_data_dict.update({'mxos_version_info':command_exc(ssh,cmd_mxos_ver,'mxos_version')})
			
			stdin, stdout, stderr =  ssh.exec_command("find / -name version.sh | grep -i tomcat")
			tomcat_version = []
			startup_path_res =stdout.readlines()
			if startup_path_res:
				for startup_path in startup_path_res:
					if not sys_data_dict.has_key("tomcat_data"):
						path = startup_path.split("version.sh")
						change_dir = path[0]
						stdin, stdout, stderr =  ssh.exec_command("cd "+change_dir+";./version.sh")
						res_tomcat_ver =stdout.readlines()
						tomcat_version+=get_output_format(res_tomcat_ver,'res_tomcat_ver')
						sys_data_dict.update({'tomcat_data':tomcat_version})
			else:
				stdin, stdout, stderr =  ssh.exec_command("rpm -qa | grep tomcat")
				tomcat_ver = stdout.readlines()
				if not tomcat_ver:
					tomcat_msg = "Tomcat Not Installed "
					tomcat_version.append('<font size="2" color="#FA5858">'+tomcat_msg+'</font>')
				else:
					tomcat_version+=get_output_format(tomcat_ver,'res_tomcat_ver')
				sys_data_dict.update({'tomcat_data':tomcat_version})
		
		# *****************************ETHERNET DATA BLOCK START ************************************
		
		stdin, stdout, stderr =  ssh.exec_command('ifconfig -s | sed \'1d\' |  cut -d " " -f 1 | sort -u')
		eth_data = []
		ethernet_devices = stdout.readlines()
		if ethernet_devices:
				for line in ethernet_devices:
					res = line.isspace()
					if res==False:
						line = line.replace("\n","<br>")
						line = line.replace("\t","&nbsp;&nbsp;&nbsp;")
						line = line.replace(" ","&nbsp;")
						eth_data.append('<font size="2" color="grey">'+line+'</font>')
		elif not ethernet_devices:
			eth_data.append('<font size="2" color="#FA5858"> Data Not Found !!!</font>')
		sys_data_dict.update({'ethernet_driver':eth_data})
		
		eth_capacity = {}
		if ethernet_devices:
			for eth_driver in ethernet_devices:
				eth_cap_lines = []
				res = eth_driver.isspace()
				if res==False:
					stdin, stdout, stderr =  ssh.exec_command("ethtool "+eth_driver+"|grep -i speed")
					speed_data = stdout.readlines()
					if speed_data:
						eth_cap_lines+=get_output_format(speed_data,'eth_cap_lines')
						eth_capacity.update({eth_driver:eth_cap_lines})
					else:
						eth_cap_lines.append('<font size="2" color="#FA5858"> No Data Available for Ethernet Capacity !!!</font>')
						eth_capacity.update({eth_driver:eth_cap_lines})

		sys_data_dict.update({'ethernet_capacity':eth_capacity})

		# *****************************ETHERNET DATA BLOCK END ************************************
		stdin, stdout, stderr =  ssh.exec_command('uname -r')
		kernel_version = stdout.read()
		if not kernel_version:
			kernel_version = "Data Not Found !!!"
			kernel_version = '<font size="2" color="#FA5858">'+kernel_version+'</font>'
		else:
			kernel_version = '<font size="2" color="grey">'+kernel_version+'</font>'
		kernel_version = single_line_formatting(kernel_version)
		sys_data_dict.update({'kernel_version':kernel_version})

		stdin, stdout, stderr =  ssh.exec_command("rpm -qa | grep -c ''")
		rpm_count = stdout.read()
		if not rpm_count:
			rpm_count = "Data Not Found !!!"
			rpm_count = '<font size="2" color="#FA5858">'+rpm_count+'</font>'
		else:
			rpm_count = '<font size="2" color="grey">'+rpm_count+'</font>'
		rpm_count = single_line_formatting(rpm_count)
		sys_data_dict.update({'rpm_info':rpm_count})
		
		stdin, stdout, stderr =  ssh.exec_command("service iptables status")
		iptables_status = stdout.read()
		if not iptables_status:
			iptables_status = "Data Not Found !!!"
			iptables_status = '<font size="2" color="#FA5858">'+iptables_status+'</font>'
		else:
			iptables_status = '<font size="2" color="grey">'+iptables_status+'</font>'
		iptables_status = single_line_formatting(iptables_status)
		sys_data_dict.update({'iptables_info':iptables_status})
		
		stdin, stdout, stderr =  ssh.exec_command('rpm -qa| grep jdk')
		java_version = stdout.read()
		if not java_version:
			java_version = "Data Not Found !!!"
			java_version = '<font size="2" color="#FA5858">'+java_version+'</font>'
		else:
			java_version = '<font size="2" color="grey">'+java_version+'</font>'
		java_version = single_line_formatting(java_version)
		sys_data_dict.update({'java_version_info':java_version})
		
		stdin, stdout, stderr =  ssh.exec_command("ulimit -Hn")
		ulimit_hn_no = stdout.read()
		if not ulimit_hn_no:
			ulimit_hn_no = "Data Not Found !!!"
			ulimit_hn_no = '<font size="2" color="#FA5858">'+ulimit_hn_no+'</font>'
		else:
			ulimit_hn_no = '<font size="2" color="grey">'+ulimit_hn_no+'</font>'
		ulimit_hn_no = single_line_formatting(ulimit_hn_no)
		sys_data_dict.update({'ulimit_hard_no_files':ulimit_hn_no})
		
		stdin, stdout, stderr =  ssh.exec_command("ulimit -Sn")
		ulimit_sn_no = stdout.read()
		if not ulimit_sn_no:
			ulimit_sn_no = "Data Not Found !!!"
			ulimit_sn_no = '<font size="2" color="#FA5858">'+ulimit_sn_no+'</font>'
		else:
			ulimit_sn_no = '<font size="2" color="grey">'+ulimit_sn_no+'</font>'
		ulimit_sn_no = single_line_formatting(ulimit_sn_no)
		sys_data_dict.update({'ulimit_soft_no_files':ulimit_sn_no})
		
		stdin, stdout, stderr =  ssh.exec_command("rpm -qa | grep irqbalance")
		irqbalance_ver = stdout.read()
		if not irqbalance_ver:
			irqbalance_ver = "Data Not Found !!!"
			irqbalance_ver = '<font size="2" color="#FA5858">'+irqbalance_ver+'</font>'
		else:
			irqbalance_ver = '<font size="2" color="grey">'+irqbalance_ver+'</font>'
		irqbalance_ver = single_line_formatting(irqbalance_ver)
		sys_data_dict.update({'irqbalance_version':irqbalance_ver})
		
		stdin, stdout, stderr =  ssh.exec_command("whereis scp")
		scp_stat = stdout.read()
		if not scp_stat:
			scp_stat = "Data Not Found !!!"
			scp_stat = '<font size="2" color="#FA5858">'+scp_stat+'</font>'
		else:
			scp_stat = '<font size="2" color="grey">'+scp_stat+'</font>'
		scp_stat = single_line_formatting(scp_stat)
		sys_data_dict.update({'scp_status':scp_stat})
		
		stdin, stdout, stderr =  ssh.exec_command("date")
		date_data = stdout.read()
		if not date_data:
			date_data = "Data Not Found !!!"
			date_data = '<font size="2" color="#FA5858">'+date_data+'</font>'
		else:
			date_data = '<font size="2" color="grey">'+date_data+'</font>'
		date_data = single_line_formatting(date_data)
		sys_data_dict.update({'date_time_timezone_data':date_data})
		
		stdin, stdout, stderr =  ssh.exec_command("uptime")
		uptime_data = stdout.read()
		if not uptime_data:
			uptime_data = "Data Not Found !!!"
			uptime_data = '<font size="2" color="#FA5858">'+uptime_data+'</font>'
		else:
			uptime_data = '<font size="2" color="grey">'+uptime_data+'</font>'
		uptime_data = single_line_formatting(uptime_data)
		sys_data_dict.update({'uptime_data':uptime_data})
		
		stdin, stdout, stderr =  ssh.exec_command('uname -a')
		uname_data = stdout.read()
		if not uname_data:
			uname_data = "Data Not Found !!!"
			uname_data = '<font size="2" color="#FA5858">'+uname_data+'</font>'
		else:
			uname_data = '<font size="2" color="grey">'+uname_data+'</font>'
		uname_data = single_line_formatting(uname_data)
		sys_data_dict.update({'uname_data':uname_data})
				
		stdin, stdout, stderr =  ssh.exec_command('lsof | wc -l')
		lsof_count = stdout.read()
		if not lsof_count:
			lsof_count = "Data Not Found !!!"
			lsof_count = '<font size="2" color="#FA5858">'+lsof_count+'</font>'
		else:
			lsof_count = '<font size="2" color="grey">'+lsof_count+'</font>'
		lsof_count = single_line_formatting(lsof_count)
		sys_data_dict.update({'lsof_count':lsof_count})

		if process_name == 'APPSUITE':
			stdin, stdout, stderr =  ssh.exec_command("/etc/init.d/httpd status")
			httpd_status = stdout.read()
			if not httpd_status:
				httpd_status = "Data Not Found !!!"
				httpd_status = '<font size="2" color="#FA5858">'+httpd_status+'</font>'
			else:
				httpd_status = '<font size="2" color="grey">'+httpd_status+'</font>'
			httpd_status = single_line_formatting(httpd_status)
			sys_data_dict.update({'httpd_status_info':httpd_status})
			
			stdin, stdout, stderr =  ssh.exec_command("/etc/init.d/open-xchange status")
			open_xchange_status = stdout.read()
			if not open_xchange_status:
				open_xchange_status = "Data Not Found !!!"
				open_xchange_status = '<font size="2" color="#FA5858">'+open_xchange_status+'</font>'
			else:
				open_xchange_status = '<font size="2" color="grey">'+open_xchange_status+'</font>'
			open_xchange_status = single_line_formatting(open_xchange_status)
			sys_data_dict.update({'open_xchange_status_info':open_xchange_status})
			
			stdin, stdout, stderr =  ssh.exec_command("/etc/init.d/mysqld status")
			mysqld_status = stdout.read()
			if not mysqld_status:
				mysqld_status = "Data Not Found !!!"
				mysqld_status = '<font size="2" color="#FA5858">'+mysqld_status+'</font>'
			else:
				mysqld_status = '<font size="2" color="grey">'+mysqld_status+'</font>'
			mysqld_status = single_line_formatting(mysqld_status)
			sys_data_dict.update({'mysqld_status_info':mysqld_status})
		
			stdin, stdout, stderr =  ssh.exec_command('rpm -qa | grep "owmessaging-appsuite-[0-9]"')
			app_suite_ver = stdout.read()
			if app_suite_ver:
				app_suite_ver = '<font size="2" color="grey">'+app_suite_ver+'</font>'
				sys_data_dict.update({'app_suite_install':'<font size="2" color="grey">App Suite Installed"</font>'})
			elif not app_suite_ver:
				app_suite_ver = "Data Not Found !!!"
				app_suite_ver = '<font size="2" color="#FA5858">'+app_suite_ver+'</font>'
				sys_data_dict.update({'app_suite_install':'<font size="2" color="grey">App Suite Not Installed</font>'})
			app_suite_ver = single_line_formatting(app_suite_ver)
			sys_data_dict.update({'app_suite_version':app_suite_ver})
		
		if process_name == 'MYSQLDB':
			stdin, stdout, stderr =  ssh.exec_command("mysql -V")
			mysql_version = stdout.read()
			if not mysql_version:
				mysql_version = "Data Not Found !!!"
				mysql_version = '<font size="2" color="#FA5858">'+mysql_version+'</font>'
			else:
				mysql_version = '<font size="2" color="grey">'+mysql_version+'</font>'
			mysql_version = single_line_formatting(mysql_version)
			sys_data_dict.update({'mysqldb_version':mysql_version})
		
		print "System Info Gathered from ", host_ip, "for process : ", process_name
		
		return sys_data_dict
	except:
		print "Exception found"
		print sys.exc_info()
	ssh.close()
	
	
def call_gen_commands(hostip_list,config_data_dict,process_name,q,ansible,mgr_mxos_ips_list,meta_blob_check):
	"""call_gen_commands Function is triggered on Ansible and Standalone mode.
	   This Function triggers generic commands function get_server_info, and each component specific functions
	   It uses host_ip, username, password from config file or host_ip from group_vars/all file, 
	   """
	print "Inside a ",process_name," Process"
	get_server_info_visits = {}
	host_sys_data_dict = {}
	sys_data_dict = {}
	mx_comp = ['MTA','MSS','IMAP','POP','IMQUEUESERV','IMEXTSERV','IMDIRSERV','IMCONFSERV','IMDIRCACHESERV','IMDIRSERVSEC','NGINX']
	for host_ip in hostip_list:
		host_user_keys = config_data_dict.keys()
		if ansible==False:
			if process_n in host_user_keys:
				host_data = config_data_dict[process_n]
			else:
				print "Please configure data for ",process_n," in config/host_info.txt"
				sys.exit(1)
			path = ''
			if host_data.has_key("username"):
				server_username = host_data["username"]
			else:
				print "Please Configure Username for Host ",host_ip
			if host_data.has_key("password"):
				server_password = host_data["password"]
			else:
				print "Please Configure Password for Host ",host_ip
			if host_data.has_key("profile_username"):
				profile_username = host_data["profile_username"]
			else:
				print "Please Configure profile username for Host ",host_ip
			if host_data.has_key("profile_password"):
				profile_password = host_data["profile_password"]
			else:
				print "Please Configure profile password for Host ",host_ip
		elif ansible==True:
			server_username = ''
			server_password = ''
			profile_username = ''
			profile_password = ''
			if process_name == 'IMMGRSERV':
				if host_ip in mgr_mxos_ips_list:
					path = config_data_dict["MXOS"]["path"]
				else:
					path = config_data_dict["mx_home"]["path"]
			if process_name in mx_comp:
				path = config_data_dict["mx_home"]["path"]
			else :
				if process_name != 'IMMGRSERV':
					print "process_name", process_name
					path = config_data_dict[process_name]["path"]
					print "path", path
		host_ip_process_key = host_ip + process_name
		if host_ip_process_key not in get_server_info_visits.keys():
			sys_data_dict = get_server_info(host_ip,server_username,server_password,process_name,ansible)
			get_server_info_visits[host_ip_process_key] = True
		else :
			print "Already have data from ", host_ip, "for process : ", process_name
			continue

		if process_name == 'MXOS':
			mxos_version = sys_data_dict['mxos_version_info']
			if not mxos_version:
				sys_data_dict.update({'mxos_install':'MXOS not Installed'})
			if mxos_version:
				sys_data_dict.update({'mxos_install':'MXOS Installed'})		
		mx_comp_dict = {'MTA':'mta','IMAP':'imapserv','POP':'popserv','MSS':'mss'}
		mx_comp_keys = mx_comp_dict.keys()
		if process_name in mx_comp_keys:
			sys_data_dict.update(mx_comp_version(host_ip,mx_comp_dict[process_name],server_username,server_password,ansible))
			if process_name == 'MTA':
				if config_data_dict.has_key('mta_spool_Dirpath'):
					spool_dir = config_data_dict['mta_spool_Dirpath']
					for each_dir in spool_dir:
						sys_data_dict.update(spool_dir_check(host_ip,server_username,server_password,each_dir,ansible))
				else:
					spool_dir_data = []
					spool_dir_data.append("Spool Directory Does not Exist !!!")
					sys_data_dict.update({'spool_dir_data': spool_dir_data})
		
		if process_name == 'CASSANDRA':
			cass_data = get_cassandra_data(host_ip,profile_username,profile_password,path,meta_blob_check,ansible)
			sys_data_dict['cassandra_version'] = cass_data['cassandra_version']
			sys_data_dict['cassandra_ring_status'] = cass_data['cassandra_ring_status']
		sys_data_dict.update(profile_data(host_ip,profile_username,profile_password,ansible,path))
		host_sys_data_dict[host_ip] = sys_data_dict
	print "Exiting Call_gen_commands!!!! for ", process_name
	q.put(host_sys_data_dict)
	return True
