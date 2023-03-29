import json
from kafka import KafkaConsumer
from config import Config


print("Starting consumer...")

print("Connecting to servers...")
print(Config.SERVER1_HOST)
print(Config.SERVER2_HOST)
print(Config.SERVER3_HOST)

consumer1 = KafkaConsumer(
    Config.SERVER1_TOPIC,
    bootstrap_servers=[Config.SERVER1_HOST],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)
consumer2 = KafkaConsumer(
    Config.SERVER2_TOPIC,
    bootstrap_servers=[Config.SERVER2_HOST],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)
consumer3 = KafkaConsumer(
    Config.SERVER3_TOPIC,
    bootstrap_servers=[Config.SERVER3_HOST],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)


print("Connected to servers.")


while True:
    for consumer in [consumer1, consumer2, consumer3]:
        print(consumer)
        messages = consumer.poll(timeout_ms=1000)
        for topic_partition, records in messages.items():
            for record in records:
                print(
                    f"Received message: {record.value} on {consumer.config['bootstrap_servers']} topic {record.topic} partition {record.partition}")
