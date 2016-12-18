# Summary
The Simple5349 library is intended to implement ISO 5349 vibration measurement. It utilizes a  3 axis analog accelerometer (the ADXL 335 running at 3.3 V is supported and tested), Arduino Uno data logger, and accompanying computer software--usually run on a laptop--to collect data from the Arduino and process the resulting acceleration data into ISO 5349 compliant values. 

#Setup
##Hardware
Hookup the ADXL 335 chip. Power it between ground and 3.3 volts on the Arduino. The X axis should be connected to the Analog 0 pin, Y to Analog 1, and Z to Analog 2. 

##Arduino
Connect the Ardunio to the computer and open. Upload "arduinoDataLogger/arduinoDataLogger.ino" to the Arduino. The easiest way to do this is to install the Arduino IDE. Open this file in the IDE, select your Arduino and board type, and click upload. The Ardunio IDE will let you know when the code has been uploaded and if the upload was successful. 

#Use
##Preparation
Before going into the field, always test the setup. This is especially important if any of your connections are remotely dodgy. When measuring tool vibration, test the sensing setup frequently. It is very easy for wires to break or become disconnected when exposed to such extreme vibration, particularly in an industrial environment. To test, collect data as described below. Begin by holding the sensor in place for at least a second. Move the sensor in a few wiggles along each orthogonal axis. Minimize movement along any other axis. Finally hold the sensor stationary for at least a second before concluding data collection. 

Visualize the resulting data. Ensure that the initial and final data have minimal noise. The middle section of data should clearly show three disturbances each in a distinct axis. There should be minimal disturbances along the other two axes as each primary disturbance occurs. 

##Data Collection
To collect data, you should have first tested the setup to ensure proper functionality. The Ardunio must be connected via USB serial. If the software claims the COM port is not available, modify the name of the COM port to that of the Arduino. Windows users will need to toggel the Windows/Linux COM port naming lines. 

To run the data collection script: 
```bash
$ python collectArduinoData.py <test number>
```
Where test number is an integer value used to denote which test we are running. This will be used in the data file name. Data will be saved in the current directory in a file named: "accelerometers<test number>.txt"

Sometimes there is random noise or data from previous data collection on the serial buffer. If this is read into your data file, simply remove the offending lines in your text editor of choice and save the file. This should only be seen at the very beginning of a data file. Anywhere else is grounds to debug. 

##Data Analysis and Visualization
Data can be visualized by running: 
```bash
$ python vibrationAnalysis.py <test number>
```

This will lead you through a series of instructions and will output a data summary file, denoted by the provided test number. To get the period, an operator should zoom the plot to a fixed time window and count the upward peaks. This can be used to determine the vibration frequency. This is used to determine the frequency weighting factor. 
