# Real-Time Weather Data Streamer

### Project Overview
This project analyzes real-time weather data, focusing on temperature and humidity levels, sourced from a streaming platform. It provides a live weather monitoring system for a specific region, generating alerts based on threshold values, and dynamically visualizing temperature and humidity changes.

### The project will involve:
- Streaming weather data via Kafka
- Processing the data for analysis
- Visualization of live temperature and humidity
- Threshold-based alerts for extreme weather conditions

### Focus
The primary goal of this project is to monitor real-time weather conditions by analyzing temperature and humidity data streams. The project will process these streams, provide live alerts when thresholds are exceeded, and visualize the data dynamically in real-time.

### Technology Stack
- Apache Kafka: Used for handling real-time streaming data. Kafka ensures scalability and robustness, allowing easy extension to support multiple data sources and consumers.
- Python: Core language for both the producer and consumer components.
- Matplotlib: Used for dynamic visualization of the data in a time series chart.
- JSON: Data format for streaming weather information (temperature and humidity).

### Set up Kafka
```
brew services start zookeeper
brew services start kafka
```

### Set up Virtual Environment
```
python3.11 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Running Producer + Consumer
```
source .venv/bin/activate
python3.11 producers.py

source .venv/bin/activate
python3.11 consumers.py
```

### Data Flow Overview
Producer generates random weather data (timestamp, temperature, humidity) in JSON format and streams it to Kafka.

Consumer consumes the data from Kafka, processes it:
- Computes rolling averages for temperature and humidity.
- Checks if the data exceeds defined thresholds (e.g., temperature > 35°C).
- Visualizes the data with a dynamic graph that updates in real-time.

The graph will show:
- X-axis: Time (from the "timestamp" field).
- Y-axis: Temperature (red line) and Humidity (blue line).

Planned Alerts:
When certain thresholds are breached (e.g., temperature > 35°C or humidity < 20%), the consumer will notify you, and you can implement SMS/email alerts as needed (this feature can be added in the alert_utils.py file).
