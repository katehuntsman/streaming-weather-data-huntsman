import matplotlib.pyplot as plt
from collections import deque

def setup_visualization():
    """Set up the initial plots for temperature and humidity."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.set_title('Temperature Over Time')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Temperature (°C)')

    ax2.set_title('Humidity Over Time')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Humidity (%)')

    return fig, ax1, ax2

def compute_rolling_average(data):
    """Compute the rolling average of a given list of data."""
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def update_plots(ax1, ax2, temperature_data, humidity_data):
    """Update the plots for temperature and humidity with new data."""
    # Compute rolling averages
    temp_avg = compute_rolling_average(temperature_data)
    humidity_avg = compute_rolling_average(humidity_data)

    # Clear the previous plots to refresh them
    ax1.clear()
    ax2.clear()

    # Plot temperature and humidity with rolling averages
    ax1.plot(range(len(temperature_data)), temperature_data, color='tab:red', label=f'Temperature (Avg: {temp_avg:.2f}°C)')
    ax2.plot(range(len(humidity_data)), humidity_data, color='tab:blue', label=f'Humidity (Avg: {humidity_avg:.2f}%)')

    # Add titles and labels to the plots
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

    # Add alert annotations for threshold breaches
    if temp_avg > 30:
        ax1.annotate(f'ALERT: {temp_avg:.2f}°C', xy=(0.95, 0.95), xycoords='axes fraction', 
                     horizontalalignment='right', verticalalignment='top', 
                     fontsize=12, color='red', weight='bold')

    if humidity_avg < 20:
        ax2.annotate(f'ALERT: {humidity_avg:.2f}%', xy=(0.95, 0.95), xycoords='axes fraction', 
                     horizontalalignment='right', verticalalignment='top', 
                     fontsize=12, color='blue', weight='bold')

    # Tight layout for better spacing
    plt.tight_layout()

def start_animation():
    """Start the dynamic updating of the plots."""
    fig, ax1, ax2 = setup_visualization()

    # Simulate dynamic updates for temperature and humidity
    temperature_data = deque(maxlen=10)
    humidity_data = deque(maxlen=10)

    def animate(i):
        # For simulation purposes, you can append random data to the deques like so:
        temperature_data.append(25 + (i % 10))  # Simulating temperature data
        humidity_data.append(50 + (i % 10))  # Simulating humidity data
        update_plots(ax1, ax2, temperature_data, humidity_data)

    ani = plt.FuncAnimation(fig, animate, interval=1000)  # Update every 1 second
    plt.show()
