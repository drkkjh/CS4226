#!/usr/bin/python

import os, sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug
from mininet.node import Host, RemoteController

class TreeTopo( Topo ):
    "Tree topology"

    def build( self ):
		# Read ring.in
		# Load configuration of Hosts, Switches, and Links
		# You can write other functions as you need.
		filename = 'star.in'
		f = open(filename, "r")
		def retrieveFileContents(f):
			# Get file contents out from file
			contents = f.read().split()
			numHosts = contents[0]
			numSwitches = contents[1]
			numLinks = contents[2]
			linkDetails = contents[3:] 
			return numHosts, numSwitches, numLinks, linkDetails			

		numHosts, numSwitches, numLinks, linkDetails = retrieveFileContents(f)
		print("Number of hosts:", numHosts)
		print("Number of switches:", numSwitches)
		print("Number of links:", numLinks)

		# Add hosts
		# > self.addHost('h%d' % [HOST NUMBER])
		for i in range(1, int(numHosts) + 1):
			self.addHost('h%d' % i)

		# Add switches
		# > sconfig = {'dpid': "%016x" % [SWITCH NUMBER]}
		# > self.addSwitch('s%d' % [SWITCH NUMBER], **sconfig)
		for j in range(1, int(numSwitches) + 1):
			sconfig = {'dpid': "%016x" % j}
			self.addSwitch('s%d' % j, **sconfig)

		# Add links
		# > self.addLink([HOST1], [HOST2])
		for k in range(int(numLinks)):
			linkDetail = linkDetails[k].split(',')
			host1 = linkDetail[0]
			host2 = linkDetail[1]
			self.addLink(host1, host2)
        
                    
topos = { 'sdnip' : ( lambda: TreeTopo() ) }

if __name__ == '__main__':
    sys.path.insert(1, '/home/sdn/onos/topos')
    from onosnet import run
    run( TreeTopo() )