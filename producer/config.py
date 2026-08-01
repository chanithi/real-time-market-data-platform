# to load configuration from .env.

from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
COINGECKO_BASE_URL = os.getenv("COINGECKO_BASE_URL")

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", "10"))