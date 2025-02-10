# utils/data_processing.py
from collections import deque

# Function to calculate rolling average
def calculate_rolling_average(data_window):
    return sum(data_window) / len(data_window) if data_window else 0
