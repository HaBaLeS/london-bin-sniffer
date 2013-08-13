from scapy.all import * 
import time

def packetHandler(pkt):
	if pkt.haslayer(Dot11ProbeReq):
		print '%s\t%s' % (time.time() , pkt.addr2)
		sys.stdout.flush()
sniff(iface="mon0", prn=packetHandler)
