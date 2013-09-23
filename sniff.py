from scapy.all import * 
from sets import Set
import time
import dbutils

#macs = Set()

ds = dbutils.SqliteDataStore('sniffer.db')



def packetHandler(pkt):
	if pkt.haslayer(Dot11ProbeReq):
		#write monster log		
		print '%s\t%s' % (time.time() , pkt.addr2)
		sys.stdout.flush()
		#macs.add(pkt.addr2)

sniff(iface="mon0", prn=packetHandler, store=0)

#while True:
#	time.sleep(1)
#	for mac in macs:
#		print mac
		
