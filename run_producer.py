from producer.api_client import CoinGeckoClient
from producer.kafka_producer import MarketEventProducer

client = CoinGeckoClient()
producer = MarketEventProducer()

events = client.get_market_data()

for event in events:
    producer.publish(event)
    print(f"Published: {event['coin_id']}")