# owm-functionaltest

Role to execute the functional test cases.

## Role configuration

For LDAP test cases below parameters are required:

1. Common parameters for all the tests
   * IP Address and Port of Primary Master Directory Server.
   * ldap_username - username to access the LDAP.
   * ldap_password - password to access the LDAP.
   * ldap_domain_name - domainname defined in LDAP.

2. Add the test user in LDAP
   * ldap_user - test user to be created.
   * ldap_user_password - password of test user.
   * ldap_mailboxId - MailboxId to be added for the test user.

3. Modify an LDAP attribute of that test user in LDAP
   * ldap_user - test user to be modified.
   * ldap_user_attr_name - name of the LDAP attribute to be modified.
   * ldap_user_attr_value - new value of that LDAP attribute.
   * ldap_operation_code - operation to be performed.

4. Modify the RDN of that test user in LDAP
   * ldap_user - test user to be created.
   * ldap_user_modrdn - a new name for the test user.

5. Delete that test user
   * ldap_user_modrdn - a new name for the test user.
