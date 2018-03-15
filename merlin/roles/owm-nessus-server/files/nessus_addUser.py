import paramiko
import sys
import os

if len(sys.argv) <4:
	print "Please Provide Username and Password as Command Line Argument !!!"
	sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]

dir_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
full_path = dir_path + "/.ssh/id_rsa"

if not os.path.exists(full_path):
	print "Please provide file .ssh/id_rsa at: ", full_path
	sys.exit(1)
		
length_args = len(sys.argv)
ip_list = []
for i in range(length_args):
	if i >=3:
		ip_list.append(sys.argv[i].rstrip('\r\n'))

print "ip_list**", ip_list

def get_nessus_install(nessus_hostIP):
	print "INSIDE get_nessus_install"
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(nessus_hostIP, username='root', key_filename=full_path)
		print "CONNECTED !!!"
		stdin, stdout, stderr =  ssh.exec_command('/opt/nessus/sbin/nessuscli adduser '+username)
		stdin.write(password)
		stdin.write('\n')
		stdin.flush()
		stdin.write(password)
		stdin.write('\n')
		stdin.flush()
		stdin.write('n')
		stdin.write('\n')
		stdin.flush()
		stdin.write('\n')
		stdin.flush()
		stdin.write('y')
		stdin.write('\n')
		
		output = stdout.readlines()
		print '\n'.join(output)
		ssh.close()
	except:
		print "Exception found"
		print sys.exc_info()
		
for nessus_hostIP in ip_list:
	get_nessus_install(nessus_hostIP)

print "Users Created !!!!"
	
