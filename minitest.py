#! /usr/bin/python

import time
from mininet.net import Mininet
# from mininet.util import createLink
net = Mininet()
h1 = net.addHost('h1')
h2 = net.addHost('h2')
s1 = net.addSwitch('s1')
c0 = net.addController('c0')

net.addLink(h1,s1)
net.addLink(h2,s1)

net.start()
print("h1 ip: " + str(h1.IP()))
print("h2 ip: " + str(h2.IP()))
net.pingAll()
net.stop()
print("End")



