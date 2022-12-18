#!/bin/python3

#Code pretty much inspired by https://pythonprogramming.net/python-matplotlib-live-updating-graphs/
# ... and https://stackoverflow.com/questions/49566331/pyserial-how-to-continuously-read-and-parse

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial

#Setup figure and subplot
fig = plt.figure()
subplot = fig.add_subplot(1,1,1)
#subplotFiltered = fig.add_subplot(1,2,1)

#Setup serial
try:
 uart = serial.Serial('/dev/ttyACM1', 9600)
except serial.serialutil.SerialException:
 print("Got a serial exception for /dev/ttyACM1, trying ACM2...");
 try:
  uart = serial.Serial('/dev/ttyACM2', 9600)
 except serial.serialutil.SerialException:
  print("Got a serial except for /dev/ttyACM2, back to square one!!!...");

historicData = []
historicDataFiltered = []

def update_graph(tokenvarNeeded):
  data = int( uart.read(5) )
  print(data)
  historicData.append(data)
  subplot.clear()
  subplot.plot(historicData, color='red')

  dataFiltered = int( uart.read(5)  )
  print(dataFiltered)
  historicDataFiltered.append(dataFiltered)
  #subplotFiltered.clear()
  #subplotFiltered.plot(historicDataFiltered)
  subplot.plot(historicDataFiltered, color='green')

#Am assuming interval is milliseconds ... 
plotResult = animation.FuncAnimation(fig, update_graph, interval=20)
plt.show()
