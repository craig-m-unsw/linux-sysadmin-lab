# Readme

A VM test lab for learning.

Requires [Vagrant](https://www.vagrantup.com/) and Hypervisor supported by [Roboxes](https://roboxes.org/).

## using

Testing Parallel SSH.

```shell
vagrant validate Vagrantfile
vagrant up
vagrant ssh pyapps
source code/venv/bin/activate
cd code
time python3 ssh-test.py
```

eof
