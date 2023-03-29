import os
import json
import time
# import logging
from config import Config
from kafka import KafkaProducer

# logging.basicConfig(level=logging.DEBUG)



BASE_DIR = "/mnt/d/kafka_node/kafkapy/"

producer1 = KafkaProducer(
    bootstrap_servers=[Config.SERVER1_HOST],
    value_serializer=lambda m: json.dumps(m).encode('ascii')
)
producer2 = KafkaProducer(
    bootstrap_servers=[Config.SERVER2_HOST],
    value_serializer=lambda m: json.dumps(m).encode('ascii')
)
producer3 = KafkaProducer(
    bootstrap_servers=[Config.SERVER3_HOST],
    value_serializer=lambda m: json.dumps(m).encode('ascii')
)


# with open(os.path.join(BASE_DIR, "stream.json")) as json_file:
#     data = json.load(json_file)
#     # rest of the code

# with open('stream.json') as json_file:
#     data = json.load(json_file)
#     print(data)


with open(os.path.join(BASE_DIR, "data_stream.json")) as json_file:
        
        data = json.load(json_file)
        for item in data:
            print(item['name'])
            producer1.send(Config.SERVER1_TOPIC, value=item)
            producer2.send(Config.SERVER2_TOPIC, value=item)
            producer3.send(Config.SERVER3_TOPIC, value=item)
            time.sleep(1)
print('produced successfully')
print('producer sent successfully . . . ')
