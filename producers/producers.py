import json
import time
import random
from kafka import KafkaProducer
from datetime import datetime

# Kafka configuration
KAFKA_TOPIC = 'weather_topic'
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']  # Replace with your Kafka server

# Create Kafka producer instance
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_weather_data():
    """Generates random weather data (temperature and humidity)."""
    temperature = round(random.uniform(-10, 40), 2)  # Temperature in Celsius
    humidity = random.randint(0, 100)  # Humidity percentage
    timestamp = datetime.now().isoformat()  # Current timestamp
    return {
        'timestamp': timestamp,
        'temperature': temperature,
        'humidity': humidity
    }

def send_weather_data():
    """Send weather data to Kafka."""
    while True:
        data = generate_weather_data()
        print(f"Generated data: {data}")  # Print generated data for debugging
        
        # Send the data to Kafka
        producer.send(KAFKA_TOPIC, value=data)
        print(f"Sent data to Kafka topic {KAFKA_TOPIC}: {data}")  # Print to confirm sending
        
        time.sleep(5)  # Send data every 5 seconds

if __name__ == "__main__":
    print("Starting the producer...")
    send_weather_data()  # Start sending data
