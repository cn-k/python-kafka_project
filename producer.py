from kafka import KafkaProducer
from kafka.errors import KafkaError

# producer = KafkaProducer(bootstrap_servers=['w1.training:9092,w2.training:9092,w3.training:9092'])
producer = KafkaProducer(bootstrap_servers='w1.training:9092,w2.training:9092,w3.training:9092', request_timeout_ms=1000000, api_version_auto_timeout_ms=1000000)
future = producer.send('streaming_topic', b'raw_bytes')
producer.flush()