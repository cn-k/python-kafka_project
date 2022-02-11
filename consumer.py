from kafka import KafkaConsumer

consumer = KafkaConsumer('streaming_topic',bootstrap_servers='w1.training:9092,w2.training:9092,w3.training:9092')
for message in consumer:
    print(message)
    print(message.value)