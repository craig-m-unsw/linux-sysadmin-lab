# linux sysadmin hack lab

A Linux VM Lab for learning and documentation. Living proof of concepts.

The virtual machine names and purposes are:

**consultant**
IT consultant, Blue Team, incident responce box. Your safe 'laptop'.

**Rand-Server 1 & 1**
Random enterprise servers. A frontend, a backend DB.

Are the misconfigurations really backdoors? What forensic material can be pulled from this machine.

**attack**
The Red Team / attack / Command and control / adversary machine.

The threat to Rand Servers.


## Setup

Get Vagrant and your Hypervisor going.

```
git clone https://github.com/craig-m-unsw/linux-sysadmin-lab.git
cd linux-sysadmin-lab
vagrant status
vagrant up
```

Roboxes will be used for a base until specific Packer/Vagrant boxes are created.
https://roboxes.org/

### exercises

The `exercises/` folder will contain documented tasks.

* https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/

### Links

* https://github.com/Kirtar22/Litmus_Test
* https://gtfobins.github.io/
* https://github.com/JohnLaTwC/Shared/blob/master/Defenders%20think%20in%20lists.%20Attackers%20think%20in%20graphs.%20As%20long%20as%20this%20is%20true%2C%20attackers%20win.md
