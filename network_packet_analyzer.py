from scapy.all import rdpcap, IP, TCP, UDP
def analyze_pcap(pcap_file):
    try:
        packets = rdpcap(pcap_file)
        print(f"Total packets: {len(packets)}\n")
        for i, packet in enumerate(packets, start=1):
            print(f"Packet #{i}")
            if IP in packet:
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                protocol = "Other"
                if TCP in packet:
                    protocol = "TCP"
                elif UDP in packet:
                    protocol = "UDP"
                print(f"Source IP      : {src_ip}")
                print(f"Destination IP : {dst_ip}")
                print(f"Protocol       : {protocol}")
                print(f"Packet Length  : {len(packet)} bytes")
                payload = bytes(packet.payload)
                if payload:
                    preview = payload[:50]
                    print(f"Payload Preview: {preview}")
                else:
                    print("Payload Preview: None")
            else:
                print("Non-IP Packet")
            print("-" * 50)
    except FileNotFoundError:
        print("PCAP file not found.")
    except Exception as e:
        print("Error:", e)
if __name__ == "__main__":
    pcap_path = input("Enter PCAP file path: ")
    analyze_pcap(pcap_path)