#!/bin/env sh

wget https://apt.puppet.com/puppet-tools-release-focal.deb

sudo dpkg -i puppet-tools-release-focal.deb
sudo apt-get update 
sudo apt-get install puppet-bolt