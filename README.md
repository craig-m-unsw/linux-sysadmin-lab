# Readme

Virtual Machine Lab for learning.

Requires [Vagrant](https://www.vagrantup.com/) and Hypervisor supported by [Roboxes](https://roboxes.org/), no other software on your host machine is required.

## using

Testing Parallel SSH connections:

```shell
vagrant validate Vagrantfile
vagrant up
vagrant ssh pyapps
source ~/venv/bin/activate
time python3 code/ssh-test.py
```

Hyper-V note: the IP's in `ssh-test.py` will need updating as no static IP can be set (platform [limitation](https://www.vagrantup.com/docs/providers/hyperv/limitations)).

