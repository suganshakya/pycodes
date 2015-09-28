#! /usr/bin/python

import time
from mininet.net import Mininet
from mininet.node import Node
from mininet.link import Link
# from mininet.util import createLink --- not working
# from mininet.topo import SingleSwitchTopo
from mininet.cli import CLI
net = Mininet()

#Creating Nodes
h1 = net.addHost('h1',ip='192.168.50.1/24')
h2 = net.addHost('h2',ip='192.168.50.2/24')
s1 = net.addSwitch('s1')
c0 = net.addController('c0')

# Setting own IP but not working
#h1.setIP('192.168.50.1/24')
#h2.setIP('192.168.50.2/24')

# Creating Links
net.addLink(h1,s1)
net.addLink(h2,s1)


net.start()
print("h1 ip: " + str(h1.IP()))
print("h2 ip: " + str(h2.IP()))
#net.dump()
print h1.cmd('ping -c1', h2.IP())
CLI(net)  # it will launch mininet> in the prompt
# net.pingAll()
net.stop()
print("End")



