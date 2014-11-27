from scapy.all import *


src_ip = "192.168.0.105"
sport = 59333
dst_ip = "64.233.167.94"
dport=80
ip_header = IP(dst=dst_ip, src=src_ip)

syn = TCP(dport=dport, sport= sport,
          ack=0, flags="S")

ans, unans = sr(ip_header / syn, timeout = 5)


ans.summary()  
index = 0
for pkts in ans:
    for pkt in pkts:
        print "PKT: ", index
        pkt.show()
        index +=1
        
ack = TCP(dport=dport, sport=sport, ack=pkts[1].seq + 1, flags="A")

ans, unans = sr(ip_header / ack, timeout = 5)

ans.summary()  
index = 0
for pkts in ans:
    for pkt in pkts:
        print "PKT: ", index
        pkt.show()
        index +=1
        
# comment        