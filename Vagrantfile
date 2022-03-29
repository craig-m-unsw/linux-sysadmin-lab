Vagrant.require_version ">= 2.2.18"

require 'yaml'

# load all server config
servers = YAML.load_file(File.join(File.dirname(__FILE__), 'inventory-vagrant.yml'))

# debug mode: true/false
indebug="false"

if indebug == "true" then puts "* vagrant starting" end

# provision ansible controller
$controller_script = <<-SCRIPT
apt update
apt install software-properties-common -y -q
add-apt-repository --yes --update ppa:ansible/ansible
apt install ansible -y -q
SCRIPT

# provision node VM
$compute_node_script = <<-SCRIPT
logger "compute node provision"
if [ ! -f /etc/ansible/facts.d/workers.fact ]; then
    echo "setup host"
    mkdir -pv /etc/ansible/facts.d/
    echo '{"compute_worker": "true"}' > /etc/ansible/facts.d/workers.fact
    # add key for ansible
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC/CRSXXVk82rJmbZGmMiiqFXwy8PARyhr/9GhWVt61BRcJlx2kL1gJpISqXmvNKnpjb8l/Sprf1Imeevuz56KX3nRbgWd9f+qaUuBYqwe9EBW7kQFHncChoMhScD97LWQvECH+dXuESWxxQm6ZuNifKmT5xFlZZm+sjJ+KQX8JSPxDzgC5fHuPwtPAXLbVEigo800gX4w15uJoVYelJJy0maTnkJBDXzlpJSVE9PZAhK3M8MrmsmCv6K4LhIyXs4hisaNHU6m0pKT0l1Stt9ZEiOzylOAtBY2Gffzp74E1j6YAJOCbftwZr366PSKClHwpmQA/ZxABdsyHBA7fahi5BaZtijWm9FHsirdxnZUWXGFTHIrSp8dqYCydcndLJ6xG08AIcRJsBgwMErBn8ilBaXpkwdnH8ChB1w4bzXLn739JRcqct7VJ61DL6jB+q4VMzTCuZ/Iksfo73rEMYbgZMTnIn35RJRkPUQXVbulJ6MXuLkI4gbcHHMDn7G3NdL0= user@host.local" >> /home/vagrant/.ssh/authorized_keys
fi
SCRIPT

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

    servers.each do |machine|
        config.vm.define machine["hostname"] do |node|

            if indebug == "true" then 
                puts "------------"
                puts "ip: #{machine["ip"]} host: #{machine["hostname"]}"
            end

            node.vm.box = machine["thebox"]
            node.vm.hostname = machine["hostname"]
            node.vm.network :forwarded_port, guest: machine["gport"], host_ip: '127.0.0.1', host: machine["hport"], protocol: "tcp"
            node.vm.network "private_network", ip: machine["ip"]

            # NOTE: no static IP on Hyper-V, platform limitation, so this will prob all break
            node.vm.provider "hyperv" do |hpv|
                hpv.memory = machine["ram"]
                hpv.cpus = machine["cpu"]
                hpv.network "public_network", bridge: "Default Network"
                hpv.network "private_network", bridge: "Default Network"
            end
            node.vm.provider "virtualbox" do |vb|
                vb.memory = machine["ram"]
                vb.cpus = machine["cpu"]
            end
            node.vm.provider "parallels" do |prl|
                prl.memory = machine["ram"]
                prl.cpus = machine["cpu"]
                prl.check_guest_tools = false
            end

            if (machine["hostname"]) == "controller"
                # ansible controller VM
                if indebug == "true" then puts "type: ansible controller" end
                node.vm.synced_folder machine["files"], "/vagrant", type: "rsync", disabled: false
                node.vm.provision :shell,
                    name: "ansible controller script",
                    inline: $controller_script,
                    :privileged => true
            else
                # compute node VM
                if indebug == "true" then puts "type: compute" end
                if File.exist?(machine["files"]) == true
                    node.vm.synced_folder machine["files"], "/vagrant", type: "rsync", disabled: false
                else
                    node.vm.synced_folder machine["files"], "/vagrant", type: "rsync", disabled: true
                end
                node.vm.provision :shell,
                    name: "user setup script",
                    inline: $compute_node_script,
                    :privileged => true
            end

            if indebug == "true" then puts "------------" end

        end
    end

    config.trigger.after [:up, :resume, :reload] do |t|
        t.info = "running inlinescript_post"
        t.run_remote = { inline: $inlinescript_post, :privileged => false }
    end

end

# -*- mode: ruby -*-
# vi: set ft=ruby :