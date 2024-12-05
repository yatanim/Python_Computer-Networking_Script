from scapy.all import ICMP, IP, sr1


target_ip="8.8.8.8"

ip_packet=IP(dst=target_ip)
icmp_packet=ICMP()

packet=ip_packet/icmp_packet

response=sr1(packet,timeout=15,verbose=False)

if response:
    print(f"successfull response from {taget_ip} and {response.summary()}")
else:
    print("failed response from {target_ip}")