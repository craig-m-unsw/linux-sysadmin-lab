# Readme

A VM test lab for learning.

Requires [Vagrant](https://www.vagrantup.com/) and Hypervisor supported by [Roboxes](https://roboxes.org/).

## using

Testing Parallel SSH.

```shell
vagrant validate Vagrantfile
vagrant up
vagrant ssh pyapps
source ~/venv/bin/activate
time python3 code/ssh-test.py
```

note: the ip in `ssh-test.py` will need updating on Hyper-V as no static IP can be set with that provider.
