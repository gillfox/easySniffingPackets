#!/usr/bin/env python
# -*- coding: utf-8 -*-

import netinfo, unittest, threading, Queue
from scapy.all import *

class TestSniffer(unittest.TestCase):

	def test_thread_sniff(self):	
		
		pack_dst = '0.0.0.0'
		pack_port = 23
		pack = IP(dst=pack_dst)/UDP(dport=pack_port)/"Unique"	
		pack.show()
		global eq_port 
		eq_port = False
		print '--------------------------------------------------'

		def send_pack(pack):
			send(pack, iface="wlan0")

		def receive_pack():
			unans = sniff(filter="udp port 23", iface="wlan0",count=1)
			global eq_port
			if unans[0].dport == pack_port:
				eq_port = True

		t1 = threading.Thread(target=receive_pack)
		t2 = threading.Thread(target=send_pack,args=pack)


		t1.start()		
		time.sleep(2)
		t2.start()

		t1.join()
		t2.join()

		self.assertTrue(eq_port)

	
if __name__ == '__main__':
	unittest.main()
