from scapy.all import *

def tcp_syn_scan(target, ports):
    print(f"Scanning {target} for open TCP ports...")
    for port in ports:
        src_port = RandShort()
        resp = sr1(IP(dst=target)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
        
        if resp is None:
            print(f"Port {port}: Filtered")
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12:  # SYN-ACK
                # Send RST to gracefully close the connection
                sr(IP(dst=target)/TCP(sport=src_port, dport=port, flags="R"), timeout=1, verbose=0)
                print(f"Port {port}: Open")
            elif resp.getlayer(TCP).flags == 0x14:  # RST-ACK
                print(f"Port {port}: Closed")
        elif resp.haslayer(ICMP):
            icmp_layer = resp.getlayer(ICMP)
            if int(icmp_layer.type) == 3 and int(icmp_layer.code) in [1, 2, 3, 9, 10, 13]:
                print(f"Port {port}: Filtered")

# Example usage
target = "127.0.0.1"
ports = [21, 22, 80, 443, 3389]
tcp_syn_scan(target, ports)
