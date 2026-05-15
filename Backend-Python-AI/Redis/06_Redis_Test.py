"""
Basic connection example.
"""

import redis
import os

from dotenv import load_dotenv

# Load ENV variables
load_dotenv()

# Read configurations
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

# Create Redis Client
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True
)

# Test connection
try:
    response = redis_client.ping()
    if response:
        print("Successfully connected to Redis.")
except redis.ConnectionError as e:
    print("Redis connection failed.")
    print(e)

# Successfully connected to Redis.