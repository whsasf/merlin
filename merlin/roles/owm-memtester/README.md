# owm-memtester

Role to install & run Memory Tester Tool.
memtester:
* Memtester is a utility that can help system administrators find memory faults. It performs stress test to find memory subsystem  faults.
* It is very effective at finding intermittent and non-deterministic faults.

## Role configuration

* memtory_size - To test the memory of a machine. The value can be in bytes, kilobytes, megabytes, or gigabytes respectively.
* number_of_iterations -  Number of loops to iterate through. Default is infinite (i.e., if this value is blank).
* report_file - To get the result of the test run by memtester tool.
