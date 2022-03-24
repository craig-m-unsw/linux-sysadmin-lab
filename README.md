# Readme

A VM test lab for learning.

Requires [Vagrant](https://www.vagrantup.com/) and Hypervisor supported by [Roboxes](https://roboxes.org/), no other software on your host machine is required.

## using

Testing Parallel SSH.

```shell
vagrant validate Vagrantfile
vagrant up
vagrant ssh pyapps
source ~/venv/bin/activate
time python3 code/ssh-test.py
```

note: the IP in `ssh-test.py` will need updating on Hyper-V as no static IP can be set with that provider (platform [limitation](https://www.vagrantup.com/docs/providers/hyperv/limitations)).

