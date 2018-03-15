# owm-iperf

Role to install  & configure iperf Stress tool. 
Iperf: used as network testing tool that can create Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) 
data streams and measure the throughput of a network that is carrying them.
Iperf features:
TCP 
* Measure bandwidth 
* Report MSS/MTU size and observed read sizes. 
* Support for TCP window size via socket buffers. 
* Multi-threaded if pthreads or Win32 threads are available. Client and server can have multiple simultaneous connections. 
UDP 
* Client can create UDP streams of specified bandwidth. 
* Measure packet loss 
* Measure delay jitter 
* Multicast capable 
* Multi-threaded if pthreads are available. Client and server can have multiple simultaneous connections
Other features
* Can run for specified time, rather than a set amount of data to transfer. 
* Server handles multiple connections, rather than quitting after a single test. 
* Print periodic, intermediate bandwidth, jitter, and loss reports at specified intervals. 
* Run the server as a daemon.


## Role configuration

* iperfserv_port (Default: 10000) - to start the iperf as a server on the specified port.
* iperf_bandwidth_to_test (Default: 10m) - to test the bandwidth for UDP, the valid suffixes are 'm' and 'k'.
* iperf_tcp_report (Default: iperf_tcp) - to save the output of iperf ran for TCP
* iperf_udp_report (Default: iperf_udp) - to save the output of iperf ran for UDP

To add more option, please refer below list:

-b  --bandwidth   for UDP, bandwidth to send at in bits/sec (default 1 Mbit/sec, implies -u) 
-d  --dualtest    Do a bidirectional test simultaneously 
-n  --num         number of bytes to transmit (instead of -t) 
-r  --tradeoff    Do a bidirectional test individually 
-t  --time        time in seconds to transmit for (default 10 secs) 
-F  --fileinput   input the data to be transmitted from a file 
-I  --stdin       input the data to be transmitted from stdin 
-L  --listenport  port to recieve bidirectional tests back on 
-P  --parallel    number of parallel client threads to run 
-T  --ttl         time-to-live, for multicast (default 1) 
