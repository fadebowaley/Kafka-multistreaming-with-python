from kafka.admin import KafkaAdminClient
from config import Config

admin_client = KafkaAdminClient(
    bootstrap_servers=[Config.SERVER1_HOST,
                       Config.SERVER2_HOST, Config.SERVER3_HOST]
)

for server_host in [Config.SERVER1_HOST, Config.SERVER2_HOST, Config.SERVER3_HOST]:
    print(f"Topics in server {server_host}:")
    topic_metadata = admin_client.list_topics()
    for topic in topic_metadata:
        if topic == '__consumer_offsets':
            continue
        print(f" - {topic}")
