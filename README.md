# linux sysadmin hack lab

A Linux VM Lab for learning and documentation. Living proof of concepts.

## Layout

The virtual machine names and purposes are:

**consultant**

IT consultant, Blue Team, incident responce box. Your safe 'laptop'.

**Rand-Server 1 & 2**

Two Random enterprise servers. A frontend, a backend DB. What Trade-off have the system administrators made for usability and security? 

Are all the misconfigurations really backdoors? What forensic material can be pulled from this machine.

**attack**

The Red Team / attack / Command and control / adversary machine.

The threat to Rand Servers.


## Setup

Get Vagrant and your Hypervisor going.

Roboxes are used for a the base VM - https://roboxes.org/

```
git clone https://github.com/craig-m-unsw/linux-sysadmin-lab.git
cd linux-sysadmin-lab
vagrant status
vagrant up
```

Configure VMs:

```
vagrant ssh consultant
```

### exercises

The `exercises/` folder will contain documented tasks.

