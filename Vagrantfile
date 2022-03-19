Vagrant.require_version ">= 2.2.18"

servers = [
    {
        :thebox => "generic/ubuntu2004",
        :hostname => "pyapps",
        :ip => "192.168.56.16",
        :files => "vm-pyapps",
        :ram => 512,
        :cpu => 1,
        :hport => 9590
    }, {
        :thebox => "generic/ubuntu2004",
        :hostname => "ubnt2004a",
        :ip => "192.168.56.17",
        :files => "vm-compute",
        :ram => 512,
        :cpu => 1,
        :hport => 9591
    }, {
        :thebox => "generic/ubuntu2004",
        :hostname => "ubnt2004b",
        :ip => "192.168.56.18",
        :files => "vm-compute",
        :ram => 512,
        :cpu => 1,
        :hport => 9592
    }
]

$inlinescript_post = <<-SCRIPT
echo '-----------------------';
uname -a;
uptime;
echo '-----------------------';
SCRIPT

Vagrant.configure("2") do |config|

    config.vm.box_check_update = false
    config.ssh.keep_alive = true
    config.ssh.compression = false
    config.ssh.forward_agent = false
    config.ssh.insert_key = true

    servers.each do |machine|
        config.vm.define machine[:hostname] do |node|

            node.vm.box = machine[:thebox]
            node.vm.hostname = machine[:hostname]
            node.vm.network :forwarded_port, guest: 9090, host_ip: '127.0.0.1', host: machine[:hport], protocol: "tcp"
            node.vm.network "private_network", ip: machine[:ip]

            if File.exist?(machine[:files]) == true
                node.vm.synced_folder machine[:files], "/vagrant", type: "rsync"
            else
                node.vm.synced_folder '.', '/vagrant', type: "rsync", disabled: true
            end

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
        ansible.galaxy_role_file = "/vagrant/requirements.yml"
        ansible.playbook = "/vagrant/playbook.yml"
        ansible.extra_vars = { ansible_python_interpreter: "/usr/bin/python3" }
        ansible.verbose = true
    end

    config.trigger.after [:up, :resume, :reload] do |t|
        t.info = "running inlinescript_post"
        t.run_remote = { inline: $inlinescript_post, :privileged => false }
    end

end
