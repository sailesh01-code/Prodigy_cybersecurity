from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        proto = packet["IP"].proto

        print(f"Source IP: {ip_src}, Destination IP: {ip_dst}, Protocol: {proto}")

        if packet.haslayer("Raw"):
            payload = packet["Raw"].load
            print(f"Payload: {payload}")

def main():
    print("Packet Sniffer started...")

    # Sniff packets and call packet_callback for each packet
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
