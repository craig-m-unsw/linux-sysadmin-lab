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
cd /vagrant/
time python3 ssh-test.py
```
