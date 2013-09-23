from scapy.all import * 
import time
import dbutils

ds = dbutils.SqliteDataStore('sniffer.db'

def packetHandler(pkt):
	if pkt.haslayer(Dot11ProbeReq):
		#print '%s\t%s' % (time.time() , pkt.addr2)
		#sys.stdout.flush()
		ds.executeAndCommit('insert into dataline values (?,?)',[time.time(),pkt.addr2])

sniff(iface="mon0", prn=packetHandler, store=0)


		
