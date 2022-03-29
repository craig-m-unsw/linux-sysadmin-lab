# Multibox Vagrant for ansible

Virtual Machine Lab for learning.

Brings up a number of "compute" machines (`vm001`, `vm002`, `vm003`... etc), as many as you have RAM for. Then starts a VM to act as an Ansible control machine, and from here run playbooks against the other VM (over SSH on an internal network).

Add hosts to `inventory-vagrant.yml` and `inventory-ansible.yml`.

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
cd /vagrant
ansible-galaxy install --role-file=requirements.yml --roles-path='/vagrant/roles' --force
ansible-playbook -i inventory-ansible.yml playbook.yml
```