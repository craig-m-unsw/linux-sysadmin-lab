#!/bin/env sh

install_bolt(){
    echo "installing Bolt"

    if [ -f /etc/debian-version ]; then
        wget https://apt.puppet.com/puppet-tools-release-focal.deb
        sudo dpkg -i puppet-tools-release-focal.deb
        sudo apt-get update 
        sudo apt-get install puppet-bolt -y -q
    fi

    if [ -f /etc/redhat-release ]; then
        wget https://yum.puppet.com/puppet-tools-release-el-8.noarch.rpm
        sudo rpm -i puppet-tools-release-el-8.noarch.rpm
        sudo yum install puppet-bolt -y
    fi

    echo "bolt installed"
}

bolt --version || install_bolt && bolt --version
