import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Visualization setup
def setup_visualization():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.set_title('Temperature Over Time')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Temperature (°C)')

    ax2.set_title('Humidity Over Time')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Humidity (%)')

    return fig, ax1, ax2

def update_plots(ax1, ax2, temperature_data, humidity_data):
    if len(temperature_data) > 0 and len(humidity_data) > 0:
        # Compute rolling averages
        temp_avg = sum(temperature_data) / len(temperature_data)
        humidity_avg = sum(humidity_data) / len(humidity_data)

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

    plt.tight_layout()

def start_animation():
    fig, ax1, ax2 = setup_visualization()

    # Simulate dynamic updates
    temperature_data = deque(maxlen=10)
    humidity_data = deque(maxlen=10)

    def animate(i):
        # For simulation purposes, you can add data to deques like so
        temperature_data.append(25 + (i % 10))  # Random values for temperature
        humidity_data.append(50 + (i % 10))  # Random values for humidity
        update_plots(ax1, ax2, temperature_data, humidity_data)

    ani = animation.FuncAnimation(fig, animate, interval=1000)  # Update every 1 second
    plt.show()

if __name__ == "__main__":
    start_animation()
