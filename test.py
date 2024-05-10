import socket
import subprocess

def get_local_ip():
    # Get the local IP address of the device
    try:
        # Use a UDP socket to get the local IP address
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))  # Google's DNS server
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    except Exception as e:
        print("Error:", e)
        return None

def scan_network(local_ip):
    # Scan the network for connected devices
    network_prefix = ".".join(local_ip.split(".")[:-1]) + "."
    connected_devices = []

    for i in range(1, 255):  # Assumes /24 subnet
        ip = network_prefix + str(i)
        if ip != local_ip:
            # Ping the IP address to check if it's reachable
            result = subprocess.call(['ping', '-c', '1', '-W', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result == 0:
                connected_devices.append(ip)

    return connected_devices

def main():
    local_ip = get_local_ip()
    if local_ip:
        print("Local IP Address:", local_ip)
        print("Scanning network for connected devices...")
        devices = scan_network(local_ip)
        if devices:
            print("Connected devices:")
            for device in devices:
                print(device)
        else:
            print("No devices found on the network.")
    else:
        print("Failed to retrieve local IP address.")

if __name__ == "__main__":
    main()
