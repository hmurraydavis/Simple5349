import pprint
import matplotlib.pyplot as plt
import numpy as np
import sys
import scipy.fftpack

plt.rcParams.update({'font.size': 16})

if len(sys.argv) <= 1:
    testNum = 0
else:
    testNum = sys.argv[1]

## Decide what plots you want the script to produce. If you're not sure, set 
## them all to 1. 
orthagonalAccelPlot = 1 ## Plot raw x, y, z accelerometer data
frequency_plots = 0 ## Plot the FFT distrabution. 

## Define the file you want it to read in from: 
fileName = 'accelerometers'+str(testNum)+'.txt'

## Open the test data file: 
f = open(fileName, 'r')

## Initialize lists for our data: 
labelsLists = []
valuesList = []

## Process accelerometer and time data into squences we can work with. This is 
## seperated by axis. It is parsed into index specific lists where index number 
## matches data from different axies in the same time reading window. 
for line in f: 
    ##  Data format:  T:10,X:397.00,Y:314.00,Z:334.00
    dataArray = line.split(',')
    
    if len(labelsLists)<=len(dataArray):
        for connectedSensor in range( len(dataArray) ):
            labelsLists.append([])
            valuesList.append([])
    
    for pinNumber, sensorData in enumerate(dataArray):
        label, value = sensorData.split(':')

        labelsLists[pinNumber].append( label )
        valuesList[pinNumber].append( float(value) )
        
#print valuesList

'''
Helper function for standard data plotting of ADC data collected with the 
Arduino. 
'''
def plotData(index, label, color='#2D4671'):
    stepTime = 47125/1000.0/100
    x = [i* (5.0/1024.0) for i in valuesList[index] ]
    #x = [i for i in valuesList[3] ]
    y = [i for i in valuesList[index] ]
    #y = np.arange(0,len(x),1)
    #print 'y is: ', y
    #y= [i * stepTime for i in y]
    plt.plot(x, y, color=color, label=label, linewidth=5)


'''
Helper function to get things into a useful list from the values generated data 
structure, given the index. 
'''
def y(n):
    return [i for i in valuesList[n] ]


## If the user wants us to, generate and show a plot of the raw sensor data  
## along the 3 axies:
if orthagonalAccelPlot:
    f, axarr = plt.subplots(3, sharex=True)

    t = [i for i in valuesList[0] ]

    axarr[0].plot(t, y(1), 
        color = '#56033c', 
        alpha=.6, 
        linewidth=4, 
        label='X')
    axarr[1].plot(t, y(2), alpha=.6, 
        linewidth=4, 
        label='Y', 
        color = '#3c5603')
    axarr[2].plot(t, y(3), 
        alpha=.6, 
        linewidth=4, 
        label='Z',
        color = '#033c56')

    for i, plot in enumerate(axarr):
        axarr[i].legend()
        #axarr[i].ylabel('Angular Position ( )', fontsize = 10)
    plt.show()
    #plt.savefig('plots/Test'+str(testNum)+'.png', bbox_inches='tight')


## Do the Foruier transform on raw data from all three axies to get the 
x_rfftRes = scipy.fftpack.rfft( y(1) )
y_rfftRes = scipy.fftpack.rfft( y(2) )
z_rfftRes = scipy.fftpack.rfft( y(3) )

## Find the max of the Fourier transform, which should be the dominant 
## frequency: 
xFreq = np.argmax(x_rfftRes[100:500])
yFreq = np.argmax(y_rfftRes[100:500])
zFreq = np.argmax(z_rfftRes[100:500])

## Let the user know the dominant frequencies we found: 
print "Max frequences with FFT along axies: "
print "\tX: ", xFreq
print "\tY: ", yFreq
print "\tZ: ", zFreq
print 

    
if frequency_plots:
    plt.clf()
    plt.plot(x_rfftRes[1:], linewidth=3, color = '#FF0101', alpha=.5, label = "X RFFT")
    plt.plot(y_rfftRes[1:], linewidth=3, color = '#494528', alpha=.5, label = "Y RFFT")
    plt.plot(z_rfftRes[1:], linewidth=3, color = '#FFBF01', alpha=.5, label = "Z RFFT")
    plt.title("Fourier Transform for Period", fontsize=22)
    plt.xlabel("Frequency (Hertz)", fontsize=18)
    plt.ylabel("Mysterious FFT Units", fontsize=18)
    plt.legend()
    plt.show()
    
    
xAvg = sum(y(1))/len(y(1))
yAvg = sum(y(2))/len(y(2))
zAvg = sum(y(3))/len(y(3))


print 'Averages along axies: ' 
print "\tX: ", xAvg
print "\tY: ", yAvg
print "\tZ: ", zAvg
print 

rmsAvg = (xAvg**2 + yAvg**2 + zAvg**2)**.5
print "RMS Value for X, Y, and Z: ", rmsAvg

####freqWeightingFactor = float(raw_input("Frequency weighting factor (from table): "))

####finalWeightedResult = freqWeightingFactor * rmsAvg

####print 
####print "Final weighted result is: ", finalWeightedResult




#def makeOrthagonalAxisPlot(start, stop, save = False):
#    f, axarr = plt.subplots(3, sharex=True)

#    t = [i for i in valuesList[0] ]

#    axarr[0].plot(t, y(1), 
#        color = '#56033c', 
#        alpha=.6, 
#        linewidth=4, 
#        label='X')
#    axarr[1].plot(t, y(2), alpha=.6, 
#        linewidth=4, 
#        label='Y', 
#        color = '#3c5603')
#    axarr[2].plot(t, y(3), 
#        alpha=.6, 
#        linewidth=4, 
#        label='Z',
#        color = '#033c56')

#    for i, plot in enumerate(axarr):
#        axarr[i].legend()
#        #axarr[i].ylabel('Angular Position ( )', fontsize = 10)
#    if save: 
#        plt.savefig('plots/Test'+str(testNum)+'.png', bbox_inches='tight')
#    else: 
#        plt.show()

#userHappynessWithResult = False
#userStart = 0 
#userEnd = len(y(0))
#while(userHappynessWithResult == False):

#print "magic: ", min(enumerate(y(0)), key=lambda x: abs(x[1]-53))

