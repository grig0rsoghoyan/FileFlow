from scapy.all import ARP, Ether, srp
import socket

def get_local_ip():
    try:
        # Use a UDP socket to get the local IP address
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))  # Google's DNS server
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    except Exception:
        try:
            # Fallback method
            local_ip = socket.gethostbyname(socket.gethostname())
            return local_ip
        except Exception as e:
            print("Error:", e)
            return None

def get_network_prefix(ip):
    # Assuming a /24 subnet
    return ".".join(ip.split(".")[:-1]) + ".0/24"

def scan_network(ip_range):
    # Create ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=False)[0]

    # Parse the results
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def main():
    local_ip = get_local_ip()
    if local_ip:
        print("Local IP Address:", local_ip)
        network_prefix = get_network_prefix(local_ip)
        print("Scanning network for connected devices...")
        devices = scan_network(network_prefix)
        if devices:
            print("Connected devices:")
            for device in devices:
                print(f"IP: {device['ip']}, MAC: {device['mac']}")
        else:
            print("No devices found on the network.")
    else:
        print("Failed to retrieve local IP address.")

if __name__ == "__main__":
    main()
