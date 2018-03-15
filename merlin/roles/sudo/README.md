# sudo

Set up the system's sudo configuration.

# Example Playbook

```
- hosts: myhost
  vars:
    sudo_users:
      # root can run any command
      - root:
          host: ALL
          runas: ALL
          tag: ''
          cmd: ALL
      # wheel group can run any command without password
      - '%wheel':
          host: ALL
          runas: ALL
          tag: NOPASSWD
          cmd: ALL
  roles:
    - sudo
```
