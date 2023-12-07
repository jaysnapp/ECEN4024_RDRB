#Random De-Random Bot

import serial, string, sys, time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import Frame
from itertools import count
import random
from matplotlib import style

plt.style.use('fivethirtyeight')

x1 = list()
y1 = list()
x2 = list()
y2 = list()

ser1 = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
ser2 = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=1)

index = count()
index2 = count()

num1 = int(input("Player 1 Choose an area of intent: "))
num2 = int(input("Player 2 Choose an area of intent: "))
    
def animate(i):
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

    ax1, ax2, = plt.gcf().get_axes()

    ax1.cla()
    ax2.cla()

    ax1.axis([0, 255, 0, 255])
    ax2.axis([0, 255, 0, 255])
    
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
    
    ax1.plot(x1, y1, 'or:')
    ax2.plot(x2, y2, 'xb-')
        
def animate1(i):
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

    ax1, ax2, = plt.gcf().get_axes()

    ax1.cla()
    ax2.cla()

    ax1.axis([0, 255, 0, 255])
    ax2.axis([0, 255, 0, 255])
    
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
    
    ax1.plot(x1, y1, 'or:')
    ax2.plot(x2, y2, 'xb-')
        
def go():
    canvas = FigureCanvasTkAgg(plt.gcf(), master=page2)
    canvas.get_tk_widget().grid(column=0, row=1)
    plt.gcf().subplots(1, 2)
    
    
root = Tk()

style1 = font.Font(size = 25)

style2 = font.Font(size = 16)

page1 = Frame(root)
page2 = Frame(root)
page3 = Frame(root)

page1.grid(row=3, columns=5, sticky="nsew")
page2.grid(row=1, columns=1, sticky="nsew")
page3.grid(row=1, columns=1, sticky="nsew")

lb1 = Label(page1, text="Player Selections Page", font = style1)
lb1.grid(row=1, column=3)

lb2 = Label(page2, text="Graph Display Page", font = style1)
#lb2.pack(pady = 20)

lb3 = Label(page3, text="Final Conclusion", font = style1)
lb3.grid(row=1, column=1)

page1.tkraise()

btn1 = Button(page1, text = "Start Game", command=lambda: page2.tkraise(), font=style2)
btn1.grid(row=3, column=3)

btna = Button(page1, text = "Single Player", command=lambda: page2.tkraise(), font=style2)
btna.grid(row=2, column=2)

btnb = Button(page1, text = "Multiplayer", command=lambda: page2.tkraise(), font=style2)
btnb.grid(row=2, column=4)

btn2 = Button(page2, text = "Begin", command=go, font=style2)
btn2.grid(row=1, column=1)

btn3 = Button(page2, text = "End Game", command=lambda: page3.tkraise(), font=style2)

canvas = FigureCanvasTkAgg(plt.gcf(), master=page2)
canvas.get_tk_widget().grid(column=0, row=1)
plt.gcf().subplots(1, 2)

root.after(50000, root.destroy)
ani = FuncAnimation(plt.gcf(), animate1, interval=10, blit=False)
root.mainloop()