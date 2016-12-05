#!/usr/bin/python

import serial
import numpy as np
import time

testNum = 0

## Serial for Linux:
arduino=serial.Serial('/dev/ttyACM0', 115200)
## Serial for windows: 
##arduino = serial.Serial('COM3', 9600, timeout=0)

write_file = 'accelerometers'+str(testNum)+'.txt'

def receiving(ser):
    '''  '''
    buffer = ''
    while True:
        read_values = ser.read(ser.inWaiting())
        if '$' in read_values:
            buffer = read_values.split('$')[-1]
        else:
            buffer = buffer + read_values
        if '\n' in buffer:
            lines = buffer.split('\n')
            return lines[-2]


#general methodology:
#   1. read in from arduino
#   2. Write to file
#   3. Begin again!
while True:
    sensor_data = receiving(arduino)
    print sensor_data
    
    with open(write_file, 'a') as f:
        f.write(sensor_data)
        f.write('\n')

