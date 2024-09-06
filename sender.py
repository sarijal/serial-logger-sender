import serial
import csv
import time
from datetime import datetime

serial_port = 'COM3'   # For WIN
# serial_port='/dev/ttyUSB1'  # For Linux

baud_rate = 115200  
csv_file = "serial_log.csv"

ser = serial.Serial(serial_port, baud_rate)

def send_data(serial_conn, data):
    serial_conn.write(data.encode())

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    
    previous_timestamp = None
    
    for row in reader:
        if row:
            timestamp_str, hex_data, plain_data = row
            
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
            
            if previous_timestamp:
                time_gap = (timestamp - previous_timestamp).total_seconds()
                
                if time_gap > 0:
                    time.sleep(time_gap)
            
            print(f"Sending at {datetime.now()}: {plain_data}")
            send_data(ser, plain_data)
            
            previous_timestamp = timestamp

ser.close()