# jdk

This role installs the latest JDK from the OWM RPM repository and removes
the potentially installed OpenJDK.

* Host specific variable:
  install_jdk_7_above - Set this variable to "true" in your host var file if you wish to install JDK version later than 7.
  
## Examples

```
    - hosts: myhost
      roles:
        - jdk
```

