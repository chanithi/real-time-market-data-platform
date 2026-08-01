from kafka import KafkaProducer
import json

from producer.config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
)


class MarketEventProducer:
    def __init__(self):
        self.topic = KAFKA_TOPIC

        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda value: json.dumps(value).encode("utf-8"),
        )

    def publish(self, event):
        self.producer.send(self.topic, value=event)
        self.producer.flush()