#!/usr/bin/python

import netinfo, unittest
from scapy.all import *

class TestClass(unittest.TestCase):
		
	def testSniffUDP(self):
		default_gateway = [route for route in netinfo.get_routes() if route['dest'] == '0.0.0.0'][0]
	
		gateway = default_gateway['gateway']
		dev = default_gateway['dev']


		packets = sniff(filter="udp",iface=dev, timeout=30)
		print "Amount of packets [UDP]: ", len(packets) 

		self.assertFalse(len(packets) < 50)

if __name__ == '__main__':
	unittest.main()
