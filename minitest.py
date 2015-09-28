#! /usr/bin/python

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

h2.cmd('python -m SimpleHTTPServer 80 &')
time.sleep(2)
print h1.cmd('curl', h2.IP())
CLI(net)
h2.cmd('kill %python')
net.stop()



