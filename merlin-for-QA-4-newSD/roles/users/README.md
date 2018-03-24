# users

Role to manage users on a system.

## Role configuration

* users_create_per_user_group (default: true) - when creating users, also
  create a group with the same username and make that the user's primary
  group.
* users_group (default: users) - if users_create_per_user_group is _not_ set,
  then this is the primary group for all created users.
* users_default_shell (default: /bin/bash) - the default shell if none is
  specified for the user.
* users_create_homedirs (default: true) - create home directories for new
  users. Set this to false is you manage home directories separately.

## Creating users

Add a users_to_add variable containing the list of users to add. A good place to put
this is in `group_vars/all` or `group_vars/groupname` if you only want the
users to be on certain machines.

The following attributes are required for each user:

* username - The user's username.
* name - The full name of the user (gecos field)
* uid - The numeric user id for the user. This is required for uid consistency
  across systems.
* password - If a hash is provided then that will be used, but otherwise the
  account will be locked
* groups - a list of additional groups for the user.
* ssh-key - This should be a list of ssh keys for the user. Each ssh key
  should be included directly and should have no newlines.

In addition, the following items are optional for each user:

* home - The user's home directory. This defaults to /home/username.
* shell - The user's shell. This defaults to /bin/bash. The default is
  configurable using the users_default_shell variable if you want to give all
  users the same shell, but it is different than /bin/bash.

Example:

    ---
    users_to_add:
      - username: imail
        name: Email Mx imail account
        home: /opt/imail
        groups: []
        uid: 1001
        ssh_key:
          - "ssh-rsa AAAAB.... foo2@machine"

## Creating groups

Add a user_groups_to_add variable containing the list of groups to add. A good place to put
this is in `group_vars/all` or `group_vars/groupname` if you only want the
users to be on certain machines


## Deleting users

The `users_to_delete` variable contains a list of users who should no longer be
in the system, and these will be removed on the next Ansible run. The format
is the same as for users to add, but the only required field is `username`.
However, it is recommended that you also keep the `uid` field for reference so
that numeric user ids are not accidentally reused.
