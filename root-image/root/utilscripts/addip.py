#!/usr/bin/env python

import os
import ipaddress

ineth0 = input('eth0: ') 
ineth1 = input('eth1: ')


if ineth0 != '' :
	ipeth0 = ipaddress.IPv4Network(ineth0)
	first = 1;
	for ip in ipeth0.hosts():
		if first == 1:
			os.system('ip route add default via ' + str(ip))
			first = 0
		else: 
			os.system('ip addr add ' + str(ip) + '/' + str(ipeth0.prefixlen) + ' dev eth0')

	os.system('ip link set eth0 up')



if ineth1 != '' :
	ipeth1 = ipaddress.IPv4Network(ineth1)
	for ip in ipeth1.hosts():
		os.system('ip addr add ' + str(ip) + ' dev eth1')

	os.system('ip link set eth1 up')


