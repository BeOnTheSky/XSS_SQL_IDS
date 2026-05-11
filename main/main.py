# from datetime import datetime
# import threading
# from scapy.all import sniff, TCP, Raw , IP
# from rawData import UpdateDb
# #from datacleaning import segment
# from kafka import KafkaConsumer, KafkaProducer
# import json
# # 定义HTTP数据包处理函数
# producer = KafkaProducer(
#     bootstrap_servers='192.168.38.11:9092,192.168.38.12:9092,192.168.38.13:9092',  # Kafka 服务器地址
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')  # 消息序列化
# )
# consumer = KafkaConsumer(
#     'bishe2',  # 监听的返回结果主题
#     bootstrap_servers='192.168.38.11:9092,192.168.38.12:9092,192.168.38.13:9092',  # Kafka 服务器地址
#     auto_offset_reset='earliest',
#     enable_auto_commit=True,
#     group_id='group-B',
#     value_deserializer=lambda x: json.loads(x.decode('utf-8'))
# )

# #ms = UpdateDb()
# def consume_messages():
#     print("消费者线程已启动...")
#     for message in consumer:
#         result = message.value
#         print(f"Received result: {result}")
# def http_packet(packet):
#     if packet.haslayer(TCP) and packet[TCP].dport == 80 and packet[IP].dst == '192.168.38.1':
#         # 检查是否有HTTP请求
#         if packet.haslayer(Raw):
#             current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#             http_payload = packet[Raw].load.decode(errors='ignore')
#             src_ip = packet[IP].src  # 获取源IP地址
#             print(f'捕获到HTTP包来自：{src_ip}\n{http_payload}\n')
#             #ms.insert_http_data(src_ip, http_payload,current_time)

#             headers, _, body = http_payload.partition("\r\n\r\n")
#             lines = headers.splitlines()
#             request_line = lines[0].split(' ')
#             method = request_line[0]
#             path = request_line[1]
#             host = packet[IP].dst

#             # 初始化请求参数
#             request_params = ""
#             url = ""
#             # 处理GET请求，直接输出path
#             if method.upper() == 'GET':
#                 print(f"Method: {method}")
#                 print(f"Host: {host}")
#                 print(f"Path: {path}")
#                 url = path
#             # 处理POST请求
#             elif method.upper() == 'POST':
#                 request_params = body  # 将请求体直接作为请求参数
#                 print(f"Method: {method}")
#                 print(f"Host: {host}")
#                 print(f"Path: {path}")
#                 print(f"Request Parameters: {request_params}")
#                 url = path + request_params
#             print(url)
#             # 发送消息
#             producer.send('bishe', {'url': url})
#             producer.flush()
# if __name__ == '__main__':
#     consumer_thread = threading.Thread(target=consume_messages)
#     consumer_thread.start()

#     threads = []
#     for _ in range(4):
#         thread = threading.Thread(target=lambda: sniff(filter="tcp port 80", prn=http_packet, store=0, iface='VMware Network Adapter VMnet8'))
#         threads.append(thread)
#         thread.start()

#     # 等待所有线程完成
#     for t in threads:
#         t.join()
#     # 开始监听网络流量
#     # print("正在监听HTTP流量...")
#     # sniff(filter="tcp port 80", prn=http_packet, store=0, iface = 'VMware Network Adapter VMnet8')


from datetime import datetime
import threading
from scapy.all import sniff, TCP, Raw, IP
from kafka import KafkaConsumer, KafkaProducer
import json
from queue import Queue

from rawData import UpdateDb
db = UpdateDb()
# 定义HTTP数据包处理函数
producer = KafkaProducer(
    bootstrap_servers='192.168.38.11:9092,192.168.38.12:9092,192.168.38.13:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

consumer = KafkaConsumer(
    'bishe2',
    bootstrap_servers='192.168.38.11:9092,192.168.38.12:9092,192.168.38.13:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='group-B',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_messages():
    print("消费者线程已启动...")
    for message in consumer:
        result = message.value
        print(f"Received result: {result}")
        if result["prediction_label"]==0:
            if db.insert_normal_data(result["predict_host"],result["prediction"],result["src_host"],result["dst_host"],result["url"],result["time"]) ==0:
                print("插入失败的正常",result)
        elif result["prediction_label"]==1:  
            if db.insert_abnormal_data(result["predict_host"],result["prediction"],result["src_host"],result["dst_host"],result["url"],result["time"]) ==0:
                print("插入失败的异常",result)

def process_packet(packet_queue):
    while True:
        packet = packet_queue.get()
        if packet is None:
            break  # 用于安全退出线程
        if packet.haslayer(TCP) and packet[TCP].dport == 80 and packet[IP].dst == '192.168.38.1':
            if packet.haslayer(Raw):
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                http_payload = packet[Raw].load.decode(errors='ignore')
                src_host = packet[IP].src
                dst_host = packet[IP].dst
                if db.insert_http_data(src_host,dst_host,http_payload,current_time)==0:
                    print("插入失败的",src_host,dst_host,http_payload,current_time)
                headers, _, body = http_payload.partition("\r\n\r\n")
                lines = headers.splitlines()
                if lines:
                    request_line = lines[0].split(' ')
                    if len(request_line) >= 2:  # 确保请求行有足够的元素
                        method = request_line[0]
                        path = request_line[1]
                        request_params = ""
                        url = ""
                        if method.upper() == 'GET':
                            url = path
                        elif method.upper() == 'POST':
                            request_params = body  # 将请求体直接作为请求参数
                            url = path + '?' + request_params  # 或按需拼接请求参数
                        #print(url)
                        # 发送消息
                        producer.send('bishe', {'url': url, 'src_host': src_host, 'dst_host': dst_host, 'time': current_time})
                        producer.flush()
                    else:
                        print(f"请求行格式错误: {lines[0]}")
                else:
                    print("未找到请求行。")
                
                
                # request_line = lines[0].split(' ')
                # method = request_line[0]
                # path = request_line[1]
                # request_params = ""
                # url = ""
                # if method.upper() == 'GET':
                #     # print(f"Method: {method}")
                #     # print(f"Host: {host}")
                #     # print(f"Path: {path}")
                #     url = path
                # elif method.upper() == 'POST':
                #     request_params = body
                #     # print(f"Method: {method}")
                #     # print(f"Host: {host}")
                #     # print(f"Path: {path}")
                #     # print(f"Request Parameters: {request_params}")
                #     url = path + request_params
                # #print(url)
                # producer.send('bishe', {'url': url,'src_host':src_host,'dst_host':dst_host,'time':current_time})
                # producer.flush()
        packet_queue.task_done()

packet_queue = Queue()

def packet_sniffer():
    sniff(filter="tcp port 80", prn=lambda x: packet_queue.put(x), store=0, iface='VMware Network Adapter VMnet8')

if __name__ == '__main__':

    consumer_thread = threading.Thread(target=consume_messages)
    consumer_thread.start()
    
    sniffer_thread = threading.Thread(target=packet_sniffer)
    sniffer_thread.start()

    worker_threads = []
    for _ in range(4):
        worker_thread = threading.Thread(target=process_packet, args=(packet_queue,))
        worker_threads.append(worker_thread)
        worker_thread.start()

    sniffer_thread.join()
    packet_queue.join()

    for _ in range(4):
        packet_queue.put(None)
        
    for worker_thread in worker_threads:
        worker_thread.join()