import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Parameters for the target simulation
initial_distance = 90  # meters
final_distance = 4  # meters
initial_speed = 20  # meters per second
final_speed = 10  # meters per second
duration = (initial_distance - final_distance) / ((initial_speed + final_speed) / 2)  # total time in seconds
num_points = 200  # number of data points to simulate

# Generate the timestamps
start_time = datetime.now()
time_interval = duration / num_points  # time between each point
timestamps = [start_time + timedelta(seconds=i*time_interval) for i in range(num_points)]

# Generate the distances (linearly decreasing from 80 to 0)
distances = np.linspace(initial_distance, final_distance, num_points)

# Generate the speeds (linearly decreasing from 50 to 20)
speeds = np.linspace(initial_speed, final_speed, num_points)

# Generate the dataframe
simulated_data = pd.DataFrame({
    'Date': timestamps,
    'TargetIndex': 1,
    'Angle': 0,
    'Distance': distances,
    'Speed': speeds,
    'Direction': 'Approaching',
    'SNR': np.random.randint(50, 300, size=num_points)  # Random SNR values
})

# Save the simulated data to a CSV file
output_file_path = '20240822_000000.csv'
simulated_data.to_csv(output_file_path, index=False)



