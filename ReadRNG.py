#Random De-Random Bot

import serial, string, sys, time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# import tkinter
# from tkinter import *
import numpy as np
import random
from matplotlib import style

# root=Tk()

# mylabel = Label(root, text="Hello")
# 
# mylabel.pack()
# 
# root.mainloop()

ts = 0.001
cd = 0.002

fig1 = plt.figure()
gs = fig1.add_gridspec(2, 2, hspace=0, wspace=0)
(ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)
ax3.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)
ax4.get_xaxis().set_visible(False)
ax4.get_yaxis().set_visible(False)
ax1.text(0.45, 0.45, '1', fontsize=32, fontweight='bold')
ax2.text(0.45, 0.45, '2', fontsize=32, fontweight='bold')
ax3.text(0.45, 0.45, '3', fontsize=32, fontweight='bold')
ax4.text(0.45, 0.45, '4', fontsize=32, fontweight='bold')
fig1.suptitle('Select your area of intent!')

plt.show(block=False)
plt.pause(0.1)

num1 = int(input("Player 1 Choose an area of intent: "))
num2 = int(input("Player 2 Choose an area of intent: "))

#Joystick Code here

plt.close()

# def countdown1(t):
#     while t > 0:
#         t -= 1
#         time.sleep(ts)
#     print(X1, "is the x1 coordinate")
#     
# def countdown2(t):
#     while t > 0:
#         t -= 1
#         time.sleep(ts)
#     print(Y1, "is the y1 coordinate")
# 
# def countdown3(t):
#     while t > 0:
#         t -= 1
#         time.sleep(ts)
#     print(X2, "is the x2 coordinate")
#     
# def countdown4(t):
#     while t > 0:
#         t -= 1
#         time.sleep(ts)
#     print(Y2, "is the y2 coordinate")
    
plt.ion()

x1 = list()
y1 = list()
x2 = list()
y2 = list()

ser1 = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
ser2 = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=1)

fig = plt.figure()
gs = fig.add_gridspec(1, 2, hspace=0, wspace=0)
(ax1, ax2) = gs.subplots(sharex='col', sharey='row')
ax1.axis([0, 255, 0, 255])
ax2.axis([0, 255, 0, 255])
fig.suptitle('Random Coordinates')

if num1==1:
        ax1.axvspan(0, 127, ymin=0.5, ymax=1, color='red', alpha=0.125)
        ax1.axhspan(128, 255, xmin=0, xmax=0.5, color='red', alpha=0.125)
if num1==2:
        ax1.axvspan(128, 255, ymin=0.5, ymax=1, color='red', alpha=0.125)
        ax1.axhspan(128, 255, xmin=0.5, xmax=1, color='red', alpha=0.125)
if num1==3:
        ax1.axvspan(0, 127, ymin=0, ymax=0.5, color='red', alpha=0.125)
        ax1.axhspan(0, 127, xmin=0, xmax=0.5, color='red', alpha=0.125)
if num1==4:
        ax1.axvspan(128, 255, ymin=0, ymax=0.5, color='red', alpha=0.125)
        ax1.axhspan(0, 127, xmin=0.5, xmax=1, color='red', alpha=0.125)

if num2==1:
        ax2.axvspan(0, 127, ymin=0.5, ymax=1, color='blue', alpha=0.125)
        ax2.axhspan(128, 255, xmin=0, xmax=0.5, color='blue', alpha=0.125)
if num2==2:
        ax2.axvspan(128, 255, ymin=0.5, ymax=1, color='blue', alpha=0.125)
        ax2.axhspan(128, 255, xmin=0.5, xmax=1, color='blue', alpha=0.125)
if num2==3:
        ax2.axvspan(0, 127, ymin=0, ymax=0.5, color='blue', alpha=0.125)
        ax2.axhspan(0, 127, xmin=0, xmax=0.5, color='blue', alpha=0.125)
if num2==4:
        ax2.axvspan(128, 255, ymin=0, ymax=0.5, color='blue', alpha=0.125)
        ax2.axhspan(0, 127, xmin=0.5, xmax=1, color='blue', alpha=0.125)

n = 5
while n > 0:

    output1 = ser1.read(1)
    output2 = ser1.read(1)
    output3 = ser2.read(1)
    output4 = ser2.read(1)

    X1=int.from_bytes(output1,byteorder=sys.byteorder)
    Y1=int.from_bytes(output2,byteorder=sys.byteorder)
    X2=int.from_bytes(output3,byteorder=sys.byteorder)
    Y2=int.from_bytes(output4,byteorder=sys.byteorder)
    
    x1.append(X1);
    y1.append(Y1);
    x2.append(X2);
    y2.append(Y2);

    ax1.plot(x1, y1, 'or:')
    ax2.plot(x2, y2, 'xb-')

    n -= 1
    
    plt.pause(0.01)
    
    if n == 0:
        print("Game complete!")
            