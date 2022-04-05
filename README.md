# Multibox Vagrant for ansible

Virtual Machine Lab for learning.

Brings up a number of "compute" machines (`vm001`, `vm002`, etc), as many as you have RAM for, then starts a VM to act as an Ansible / puppet-bolt / python-script control machine.

Set hosts in `inventory-vagrant.yml` and `inventory-ansible.yml`.

## setup

You need Vagrant, and then one of these hypervisors:

* virtual box
* parallels
* vmware desktop
* libvirt

Using Hyper-V will not work because of network [limitations](https://www.vagrantup.com/docs/providers/hyperv/limitations).

```shell
vagrant validate vagrantfile
vagrant up
```

## using

Login to the controller VM and run ansible.

```shell
vagrant ssh controller
cd /vagrant/ansible
ansible-galaxy install --role-file="/vagrant/ansible/requirements.yml" --roles-path="/vagrant/ansible/roles" --force
ansible-playbook -i inventory-ansible.yml playbook.yml
```
