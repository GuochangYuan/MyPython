#!/bin/bash
route add -net 10.0.0.0 netmask 255.255.255.0 gw 192.168.150.1
route add default gw 192.168.150.1 
iptables -A FORWARD -i p2p-wlp3s0-0 -j ACCEPT
iptables -A FORWARD -o p2p-wlp3s0-0 -j ACCEPT
iptables -t nat -A POSTROUTING -o wlp3s0 -j MASQUERADE
