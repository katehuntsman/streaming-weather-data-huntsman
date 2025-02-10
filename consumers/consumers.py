import json
import time
from kafka import KafkaConsumer
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from visualization import update_plots  # Import visualization functions

# Kafka configuration
KAFKA_TOPIC = 'weather_topic'
KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']

# Create Kafka consumer instance
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',  # Start from the earliest message
    group_id=None
)

# Deques to store the last 10 readings for temperature and humidity
temperature_data = deque(maxlen=10)
humidity_data = deque(maxlen=10)

# Visualization setup
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
ax1.set_title('Temperature Over Time')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Temperature (°C)')
ax2.set_title('Humidity Over Time')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Humidity (%)')

# Helper function to compute rolling average
def compute_rolling_average(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

# Function to handle threshold checks and visualization updates
def consume_messages():
    print(f"Consuming messages from topic '{KAFKA_TOPIC}'...")

    # Matplotlib interactive mode for real-time updating
    plt.ion()

    for message in consumer:
        data = message.value
        timestamp = data.get('timestamp')
        temperature = data.get('temperature')
        humidity = data.get('humidity')

        # Print received data
        print(f"Received message - Timestamp: {timestamp}, Temp: {temperature}°C, Humidity: {humidity}%")

        # Add data to the respective deques
        temperature_data.append(temperature)
        humidity_data.append(humidity)

        # Threshold alerts (example)
        if temperature > 35:
            print(f"ALERT: Temperature exceeds 35°C! ({temperature}°C)")
        if humidity < 20:
            print(f"ALERT: Humidity is below 20%! ({humidity}%)")

        # Update the plot with the latest data
        update_plots(ax1, ax2, temperature_data, humidity_data)
        
        # Pause to allow for interactive updating
        plt.pause(0.1)

if __name__ == "__main__":
    # Start consuming and plotting
    consume_messages()
