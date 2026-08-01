from producer.api_client import CoinGeckoClient

client = CoinGeckoClient()

data = client.get_market_data()

print(data)