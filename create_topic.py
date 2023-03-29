from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError
from config import Config

admin_client = KafkaAdminClient(
    bootstrap_servers=[Config.SERVER1_HOST,
                       Config.SERVER2_HOST, 
                       Config.SERVER3_HOST
                       ]
)



topics = [
    NewTopic(name=Config.SERVER1_TOPIC,
             num_partitions=1, replication_factor=1),
    NewTopic(name=Config.SERVER2_TOPIC,
             num_partitions=1, replication_factor=1),
    NewTopic(name=Config.SERVER3_TOPIC,
             num_partitions=1, replication_factor=1),
]

try:
    topic_futures = admin_client.create_topics(
        new_topics=topics, validate_only=False)
    for topic, future in topic_futures.items():
        future.result()
        print(f"Topic {topic} created successfully.")
except TopicAlreadyExistsError as e:
    print(f"Failed to create topics: {e}")
except Exception as e:
    print(f"Failed to create topics: {e}")


