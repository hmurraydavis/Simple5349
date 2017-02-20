#!/usr/bin/python

import serial
import sys

## Let us input the test number from the command line when we run the code. 
## If no test number is provided, use a default test number:
if len(sys.argv) <= 1:
    testNum = 37
else:
    testNum = sys.argv[1]


## Establish the serial connection to the data logger: (Uncomment for your OS)
## Serial for Linux:
arduino=serial.Serial('/dev/ttyACM0', 115200)
## Serial for Windows: 
##arduino = serial.Serial('COM3', 9600, timeout=0)


## Form our file name in standard form with the test number:
write_file = 'accelerometers'+str(testNum)+'.txt'


def receiving(ser):
    '''
    Receive data sent from the data logger over a serial connection. 
    Waits until a $ character is seen on the serial connection. This denotes 
    the start of a data string and prevents us from reading in partial strings 
    of data. Grabs characters sent back until a new line character (terminal 
    character in the data string format used) is received. Returns the data 
    string (as a string), removing the initial, begining of string deliniating 
    characters.
    '''
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

## Service loop to collect data from the data logger: 
# general methodology:
#   1. read in from arduino
#   2. Write to file
#   3. Begin again!
while True:
    sensor_data = receiving(arduino)
    print sensor_data
    
    with open(write_file, 'a') as f:
        f.write(sensor_data)
        f.write('\n')

