# to fetch data from CoinGecko.
# It should not know anything about Kafka.

# HTTP request
# Authentication
# Timeout
# Error handling
# Return clean Python data

import requests

from producer.config import (
    COINGECKO_API_KEY,
    COINGECKO_BASE_URL
)


class CoinGeckoClient:
    """
    Client responsible for retrieving market data from CoinGecko.
    """

    def __init__(self):
        self.base_url = COINGECKO_BASE_URL

        self.headers = {
            "x-cg-demo-api-key": COINGECKO_API_KEY
        }

    def get_market_data(self):

        endpoint = f"{self.base_url}/coins/markets"

        params = {
            "vs_currency": "usd",
            "ids": "bitcoin,ethereum,solana",
            "order": "market_cap_desc",
            "per_page": 3,
            "page": 1,
            "sparkline": "false"
        }

        response = requests.get(
            endpoint,
            headers=self.headers,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        events = []

        for coin in response.json():
            events.append({
                "event_time": coin["last_updated"],
                "coin_id": coin["id"],
                "symbol": coin["symbol"],
                "name": coin["name"],
                "currency": "usd",
                "price": coin["current_price"],
                "market_cap": coin["market_cap"],
                "volume_24h": coin["total_volume"],
                "price_change_24h": coin["price_change_24h"],
                "price_change_percentage_24h": coin["price_change_percentage_24h"],
            })

        return events