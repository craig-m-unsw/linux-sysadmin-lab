#!/usr/bin/env python3

import ipaddress
import socket
import struct
import platform
import socket
from csv import reader
from pssh.clients import ParallelSSHClient
from pssh.config import HostConfig


the_hosts = ['192.168.60.11', '192.168.60.12']
# todo: read /vagrant/inventory-ansible.yml

the_cmd = "hostname; sleep 5; echo ok;"

client = ParallelSSHClient(the_hosts, user='vagrant', pkey='/vagrant/id_rsa')


if __name__ == '__main__':
    print("running command\n")
    output = client.run_command(the_cmd)
    for host_output in output:
        for line in host_output.stdout:
            print(line)
        exit_code = host_output.exit_code
        print("Host %s exit code: %s\n" % (host_output.host, host_output.exit_code))
    print("\nfinished\n")
