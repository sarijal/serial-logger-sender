import serial
from datetime import datetime
import csv

serial_port = 'COM6'   # For WIN
# serial_port='/dev/ttyUSB1'  # For Linux

baud_rate = 115200  
output_file = "serial_log.csv" 

ser = serial.Serial(serial_port, baud_rate, timeout=0.01)
  
while True:
    data = ser.readline().strip() 
    
    if data:
        timestamp = datetime.now() 
        
        hex_data = data.hex()  
        
        with open(output_file, 'a', newline='') as file:
            writer = csv.writer(file)
            print(f"Time: {timestamp}, Data (Hex): {hex_data}, Data : {data}")
            writer.writerow([timestamp, hex_data, data.decode('utf-8', 'ignore')])

ser.close()