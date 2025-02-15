import json
import time
from kafka import KafkaConsumer
from collections import deque
import matplotlib.pyplot as plt
from datetime import datetime

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
def update_plots(ax1, ax2, temperature_data, humidity_data):
    # Compute rolling averages
    temp_avg = compute_rolling_average(temperature_data)
    humidity_avg = compute_rolling_average(humidity_data)

    # Clear previous data
    ax1.clear()
    ax2.clear()

    # Plot temperature and humidity with rolling averages
    ax1.plot(range(len(temperature_data)), temperature_data, color='tab:red', label=f'Temperature (Avg: {temp_avg:.2f}°C)')
    ax2.plot(range(len(humidity_data)), humidity_data, color='tab:blue', label=f'Humidity (Avg: {humidity_avg:.2f}%)')

    # Add titles and labels
    ax1.set_title(f'Temperature Over Time (Avg: {temp_avg:.2f}°C)', fontsize=14)
    ax1.set_xlabel('Time (s)', fontsize=12)
    ax1.set_ylabel('Temperature (°C)', fontsize=12)

    ax2.set_title(f'Humidity Over Time (Avg: {humidity_avg:.2f}%)', fontsize=14)
    ax2.set_xlabel('Time (s)', fontsize=12)
    ax2.set_ylabel('Humidity (%)', fontsize=12)

    # Add gridlines and legends
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax1.legend(loc='upper left', fontsize=10)
    ax2.legend(loc='upper left', fontsize=10)

    # Tight layout for better spacing
    plt.tight_layout()

def consume_messages():
    print(f"Consuming messages from topic '{KAFKA_TOPIC}'...")

    # Matplotlib interactive mode for real-time updating
    plt.ion()

    for message in consumer:
        data = message.value
        timestamp = data.get('timestamp')
        temperature = data.get('temperature')
        humidity = data.get('humidity')

        print(f"Received message - Timestamp: {timestamp}, Temp: {temperature}°C, Humidity: {humidity}%")

        # Append new data to deques
        temperature_data.append(temperature)
        humidity_data.append(humidity)

        # Check for threshold conditions and annotate alerts
        if temperature > 30:
            ax1.annotate(f'ALERT: {temperature}°C', xy=(0.95, 0.95), xycoords='axes fraction', 
                         horizontalalignment='right', verticalalignment='top', 
                         fontsize=12, color='red', weight='bold')

        if humidity < 20:
            ax2.annotate(f'ALERT: {humidity}%', xy=(0.95, 0.95), xycoords='axes fraction', 
                         horizontalalignment='right', verticalalignment='top', 
                         fontsize=12, color='blue', weight='bold')

        # Update the plots with new data
        update_plots(ax1, ax2, temperature_data, humidity_data)

        # Pause briefly to allow for the real-time update to appear
        plt.pause(0.1)

if __name__ == "__main__":
    # Start consuming and plotting
    consume_messages()
