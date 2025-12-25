import socket
import struct
import textwrap
from scapy.all import sniff

# Indentation variables for clean output
TAB_1 = '\t - '
TAB_2 = '\t\t - '
TAB_3 = '\t\t\t - '
TAB_4 = '\t\t\t\t - '

DATA_TAB_1 = '\t '
DATA_TAB_2 = '\t\t '
DATA_TAB_3 = '\t\t\t '
DATA_TAB_4 = '\t\t\t\t '

def main():
    print("[*] Starting Complete Network Sniffer...")
    print("[*] Waiting for packets (Press Ctrl+C to stop)...")
    sniff(prn=analyze_packet, store=0)

def analyze_packet(packet):
    # 1. Get raw bytes
    raw_data = bytes(packet)

    # 2. Parse Ethernet Header
    eth_header = raw_data[:14]
    dest_mac, src_mac, eth_proto = get_ethernet_header(eth_header)
    
    print('\n' + 'Ethernet Frame:')
    print(TAB_1 + f'Destination: {dest_mac}, Source: {src_mac}, Protocol: {eth_proto}')

    # 3. Check for IPv4 (Protocol 2048 is 0x0800)
    if eth_proto == 2048:
        ip_header = raw_data[14:34]
        version, header_length, ttl, proto, src, target = get_ip_header(ip_header)

        print(TAB_1 + 'IPv4 Packet:')
        print(TAB_2 + f'Version: {version}, Header Length: {header_length}, TTL: {ttl}')
        print(TAB_2 + f'Protocol: {proto}, Source: {src}, Target: {target}')

        # 4. Check for TCP (Protocol 6)
        if proto == 6:
            tcp_raw = raw_data[34:54]
            # Safety check: make sure we have enough bytes for a header
            if len(tcp_raw) == 20:
                src_port, dest_port, seq, ack = get_tcp_header(tcp_raw)
                print(TAB_1 + 'TCP Segment:')
                print(TAB_2 + f'Source Port: {src_port}, Destination Port: {dest_port}')
                print(TAB_2 + f'Sequence: {seq}, Acknowledgment: {ack}')

        # 5. Check for UDP (Protocol 17)
        elif proto == 17:
            udp_raw = raw_data[34:42]
            # Safety check
            if len(udp_raw) == 8:
                src_port, dest_port, length = get_udp_header(udp_raw)
                print(TAB_1 + 'UDP Segment:')
                print(TAB_2 + f'Source Port: {src_port}, Destination Port: {dest_port}, Length: {length}')

        # 6. Print Payload (Hex + ASCII)
        # We assume the payload starts after byte 34 for simplicity
        # (This is a simplified view; technically TCP header size varies)
        print(TAB_1 + 'Payload Data (Hex):')
        print(format_multi_line(DATA_TAB_2, raw_data[34:]))
        
        print(TAB_1 + 'Payload Data (ASCII):')
        print(DATA_TAB_2 + get_ascii_payload(raw_data[34:]))

# --- HELPER FUNCTIONS ---

def get_ethernet_header(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data)
    # NOTE: We return the raw protocol (2048) here, NOT htons
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), proto

def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

def get_ip_header(data):
    store_obj = struct.unpack('!BBHHHBBH4s4s', data)
    _version_ihl = store_obj[0]
    version = _version_ihl >> 4
    ihl = _version_ihl & 0xF
    ih_len = ihl * 4
    ttl = store_obj[5]
    proto = store_obj[6]
    src = socket.inet_ntoa(store_obj[8])
    target = socket.inet_ntoa(store_obj[9])
    return version, ih_len, ttl, proto, src, target

def get_tcp_header(data):
    store_obj = struct.unpack('!HHLLBBHHH', data)
    src_port = store_obj[0]
    dest_port = store_obj[1]
    sequence = store_obj[2]
    acknowledgment = store_obj[3]
    return src_port, dest_port, sequence, acknowledgment

def get_udp_header(data):
    store_obj = struct.unpack('!HHHH', data)
    src_port = store_obj[0]
    dest_port = store_obj[1]
    length = store_obj[2]
    return src_port, dest_port, length

def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])

def get_ascii_payload(data):
    ascii_string = ''.join([chr(byte) if 32 <= byte <= 126 else '.' for byte in data])
    return ascii_string

if __name__ == "__main__":
    main()