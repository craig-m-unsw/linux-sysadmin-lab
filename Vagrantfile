Vagrant.require_version ">= 2.2.18"

#
# VM config
#

servers = [
    {
        :hostname => "pyapps",
        :thebox => "generic/ubuntu2004",
        :ip => "192.168.56.16",
        :files => "vm-pyapps",
        :ram => 512,
        :cpu => 1,
        :hport => 9590
    }, {
        :hostname => "ubnt2004a",
        :thebox => "generic/ubuntu2004",
        :ip => "192.168.56.17",
        :files => "vm-compute",
        :ram => 512,
        :cpu => 1,
        :hport => 9591
    }, {
        :hostname => "ubnt2004b",
        :thebox => "generic/ubuntu2004",
        :ip => "192.168.56.18",
        :files => "vm-compute",
        :ram => 512,
        :cpu => 1,
        :hport => 9592
    }
]

ANSIBLE_GROUPS = {
    # set groups:
    "pyappgroup" => ["pyapps"],
    "compute" => ["ubnt2004a", "ubnt2004b"],
    # group vars:
    "pyappgroup:vars" => {
        "vm_comment" => "main control node",
        "py_nodes" => "192.168.17,192.168.18"
    },
    "compute:vars" => {
        "vm_comment" => "worker/compute node"
    }
}

ANSIBLE_EXTRAVAR = {
    ansible_python_interpreter: "/usr/bin/python3",
    foo_vers: "v1.0 beta",
    vm_range: "192.168.56.*"
}

#
# Vagrant starts (no config below here)
#

$inlinescript_post = <<-SCRIPT
echo '-----------------------';
uname -a;
uptime;
echo '-----------------------';
SCRIPT

Vagrant.configure("2") do |config|

    config.ssh.keep_alive = true
    config.ssh.compression = false
    config.ssh.forward_agent = false
    config.ssh.insert_key = true
    config.vm.box_check_update = false
    config.vm.synced_folder "./ansible/", "/vagrant", type: "rsync"

    servers.each do |machine|
        config.vm.define machine[:hostname] do |node|

            node.vm.box = machine[:thebox]
            node.vm.hostname = machine[:hostname]
            node.vm.network :forwarded_port, guest: 9090, host_ip: '127.0.0.1', host: machine[:hport], protocol: "tcp"
            node.vm.network "private_network", ip: machine[:ip]

            # if folder exists then upload
            if File.exist?(machine[:files]) == true
                node.vm.synced_folder machine[:files], "/home/vagrant/code", type: "rsync"
            else
                node.vm.synced_folder machine[:files], "/home/vagrant/code", type: "rsync", disabled: true
            end

            # NOTE: no static IP on Hyper-V, the 'ip' setting will be ignored.
            node.vm.provider "hyperv" do |hpv|
                hpv.memory = machine[:ram]
                hpv.cpus = machine[:cpu]
                hpv.network "public_network", bridge: "Default Network"
                hpv.network "private_network", bridge: "Default Network"
            end
            node.vm.provider "virtualbox" do |vb|
                vb.memory = machine[:ram]
                vb.cpus = machine[:cpu]
            end
            node.vm.provider "parallels" do |prl|
                prl.memory = machine[:ram]
                prl.cpus = machine[:cpu]
                prl.check_guest_tools = false
            end

        end
    end

    config.vm.provision "ansible_local" do |ansible|
        ansible.playbook = "/vagrant/playbook.yml"
        ansible.galaxy_role_file = "/vagrant/requirements.yml"
        ansible.groups = ANSIBLE_GROUPS
        ansible.extra_vars = ANSIBLE_EXTRAVAR
        ansible.verbose = true
    end

    config.trigger.after [:up, :resume, :reload] do |t|
        t.info = "running inlinescript_post"
        t.run_remote = { inline: $inlinescript_post, :privileged => false }
    end

end

# -*- mode: ruby -*-
# vi: set ft=ruby :