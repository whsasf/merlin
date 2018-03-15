# owm-redis

Role to install Redis on a system. 

## Role configuration
No configuration available at the moment.

## Redis tests
* Check /etc/redis.conf is changed on all nodes in order to bind to ANY: "bind 0.0.0.0"
* Check /etc/redis.conf is changed on all slave nodes in order to work as slave of the designed master: "slaveof 10.237.235.139 6379"
* Check redis and redis-sentinel services are running: "systemctl status redis redis-sentinel"
* Check redis slaves are reported (master is not included in the output): "redis-cli -p 26379 SENTINEL slaves mymaster|grep -A1 name"
* Check redis sentinels are working (every node will report other nodes instances): "redis-cli -p 26379 SENTINEL sentinels mymaster|grep -A1 name"

