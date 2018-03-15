# owm-homepermissions

Role to fix the othership for the homedir (when it is provided as a dedicated mount point) and fix
the access to the external path not owned by the service users.
This role has to be executed after the users role, once the accounts on the host have been create. .home field will be checked and fixed.

## Role configuration

This role check and fix the home from the users node managed by the role "users"

---
users:
  - username: imail
	name: Email Mx imail account
	home: /opt/imail <------- homepermissions will chown to username:group
	groups: []
	uid: 1001
	ssh_key:
	  - "ssh-rsa AAAAB.... foo2@machine"

# path below will be changed in order to gran read-access to all (chmod 0755)
required_paths:
  - /opt/blob1
  - /opt/blob2
  - /opt/blob3
