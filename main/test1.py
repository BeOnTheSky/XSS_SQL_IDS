from scapy.all import sniff, TCP, Raw, IP
from queue import Queue
from datetime import datetime

# def process_packet(packet_queue):
#     while True:
#         packet = packet_queue.get()
#         if packet is None:
#             break  # 用于安全退出线程
#         if packet.haslayer(TCP) and packet[TCP].dport == 80 and packet[IP].dst == '192.168.38.1':
#             if packet.haslayer(Raw):
#                 http_payload = packet[Raw].load.decode(errors='ignore')
#                 headers, _, body = http_payload.partition("\r\n\r\n")
#                 lines = headers.splitlines()
#                 request_line = lines[0].split(' ')
#                 method = request_line[0]
#                 path = request_line[1]
#                 url = ""

#                 if method.upper() == 'GET':
#                     url = path
#                 elif method.upper() == 'POST':
#                     request_params = body
#                     url = path + request_params

#                 print(url)  # 打印URL
#         packet_queue.task_done()

from scapy.all import sniff, TCP, Raw, IP

def process_packet(packet):
    if packet.haslayer(TCP) and packet[TCP].dport == 80 and packet[IP].dst == '192.168.38.1':
        if packet.haslayer(Raw):
            http_payload = packet[Raw].load.decode(errors='ignore')
            print(f'{http_payload}\n')
            headers, _, body = http_payload.partition("\r\n\r\n")
            lines = headers.splitlines()
            request_line = lines[0].split(' ')
            method = request_line[0]
            path = request_line[1]
            url = ""

            if method.upper() == 'GET':
                url = path
            elif method.upper() == 'POST':
                request_params = body
                url = path + request_params

            print(url)  # 打印URL

def packet_sniffer():
    sniff(filter="tcp port 80", prn=process_packet, store=0, iface='VMware Network Adapter VMnet8')

if __name__ == '__main__':
    print('开始')
    packet_sniffer()