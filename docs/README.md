# Readme

Random documentation.

## Tasks

### network

#### Block hosts

Ways to block a host.

Login to `ubnt2004a` and block `pyapps` with one of these methods.

```shell
vagrant ssh ubnt2004a
sudo su
```

Arp:

```
# set a bogus arp address (for IPs in local subnet only)
arp -s 192.168.56.16 00:00:00:00:00:01

# remove
arp -d 192.168.56.16
```

Blackhole route:

```
# null route a host
ip route add blackhole 192.168.56.16/32

# remove
ip route delete 192.168.56.16/32
```

Firewall:

```
# iptables
iptables -I INPUT -s 192.168.56.16 -j DROP
iptables -I OUTPUT -d 192.168.56.16 -j DROP

# remove (all rules)
iptables -F
```

