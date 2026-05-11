from kafka import KafkaConsumer, KafkaProducer
import json
import datacleaning
def process_url(url):
    question_mark_index = url.find('?')
    # 如果找到?，返回其后面的部分；否则返回空字符串
    if question_mark_index != -1:
        url2 =url[question_mark_index + 1:]
    else:
        url2 = ""
    payload = datacleaning.segment(url2)
    print(payload)
    payload = datacleaning.tonumpy(payload,datacleaning.fasttext["embeddings"])
    prediction,prediction_label = datacleaning.predecit(payload)
    return {'url':url,'predict_host':'computer2','prediction':prediction,'prediction_label':prediction_label}

def consume_requests():
    # 创建 Kafka 消费者
    consumer = KafkaConsumer(
        'bishe',  # 监听的主题
        bootstrap_servers='192.168.38.11:9092,192.168.38.12:9092,192.168.38.13:9092',  # Kafka 服务器地址
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='group-A',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    # 创建 Kafka 生产者用于发送结果
    producer = KafkaProducer(
        bootstrap_servers='192.168.38.11:9092,192.168.38.12:9092,192.168.38.13:9092', # Kafka 服务器地址
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    for message in consumer:
        url = message.value['url']
        print(f"Received URL to process: {url}")
        dst_host = message.value['dst_host']
        src_host = message.value['src_host']
        time = message.value['time']
        # 处理URL
        result = process_url(url)
        result['dst_host'] = dst_host
        result['src_host'] = src_host
        result['time'] = time
        print(f"Processed result: {result}")
        
        # 发送结果回主机A
        producer.send('bishe2', result)  # 发送结果到指定主题
        producer.flush()

if __name__ == "__main__":
    consume_requests()