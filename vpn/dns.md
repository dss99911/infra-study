# DNS
https://aws.amazon.com/route53/what-is-dns/

## DNS server

### find currently using dns server ip
````shell
cat /etc/resolv.conf
scutil --dns
````

### find ip address from DNS server
```shell

# showing DNS server and the host's ip address
nslookup google.com
# showing hosting record detail
dig google.com
# using specific dns server
dig google.com @168.126.63.1
```

## Routing policy
### geo location
able to map domain name to different ip address by different region 


## VPN
when connecting VPN, VPN client can change `/etc/resolv.conf` to use different DNS server

### Routing table
VPN can whitelist specific destination ip addresses to use VPN network.
- if you want your device access DNS server from VPN server. need to add the DNS server to whitelist of ip address of VPN

the Ip addresses are reflected on the device's routing table.

checking routing table
- it shows destination ip and network interface to use
- on Mac, VPN network interface named like 'utun3'
```shell
netstat -rn
```

network interface detail
```shell
ifconfig -v
```