#!/usr/bin/env python3

# time python3 ssh-test.py

import ipaddress
import socket
import struct
import platform
import socket
from pssh.clients import ParallelSSHClient
from pssh.config import HostConfig

the_hosts = ['192.168.56.17', '192.168.56.18']
the_cmd = "hostname; sleep 5; echo ok;"

client = ParallelSSHClient(the_hosts, user='compute', pkey='/home/vagrant/.ssh/id_rsa')

if __name__ == '__main__':
    print("running command\n")
    output = client.run_command(the_cmd)
    for host_output in output:
        for line in host_output.stdout:
            print(line)
        exit_code = host_output.exit_code
        print("Host %s exit code: %s\n" % (host_output.host, host_output.exit_code))
    print("\nfinished\n")
