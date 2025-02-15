import matplotlib.pyplot as plt
from collections import deque

def setup_visualization():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.set_title('Temperature Over Time')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Temperature (°C)')

    ax2.set_title('Humidity Over Time')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Humidity (%)')

    return fig, ax1, ax2

def update_plots(ax1, ax2, temperature_data, humidity_data, temperature, humidity):
    # Compute rolling averages
    temp_avg = sum(temperature_data) / len(temperature_data) if len(temperature_data) > 0 else 0
    humidity_avg = sum(humidity_data) / len(humidity_data) if len(humidity_data) > 0 else 0

    # Clear and update the plots
    ax1.clear()
    ax2.clear()

    ax1.plot(range(len(temperature_data)), temperature_data, color='red', label='Temperature (°C)')
    ax2.plot(range(len(humidity_data)), humidity_data, color='blue', label='Humidity (%)')

    ax1.set_title(f'Temperature Over Time (Avg: {temp_avg:.2f}°C)')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Temperature (°C)')

    ax2.set_title(f'Humidity Over Time (Avg: {humidity_avg:.2f}%)')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Humidity (%)')

    ax1.legend()
    ax2.legend()

    # Display the current alert status on the plot
    ax1.text(0.5, 0.95, f'ALERT: Temp = {temperature}°C', ha='center', va='center', color='red', transform=ax1.transAxes)
    ax2.text(0.5, 0.95, f'ALERT: Humidity = {humidity}%', ha='center', va='center', color='blue', transform=ax2.transAxes)

    plt.tight_layout()
