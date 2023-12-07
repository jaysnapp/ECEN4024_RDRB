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

#plt.ion()

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

# def StrtGm():
#     page2.tkraise()
#     m = 0
#     m = m + 1

# x = int
# m = 0

# def StartG():
#     btn1.pack_forget()
#     x = m+1
#     page2.tkraise()

# def graph_win():
#     root1 = tk.Tk()
#     root1.wm_title("Graph")
    
#     f = Figure(figsize=(5,4), dpi=100)
#     ax1 = f.add_subplot(111)
    
def animate(i):
#     if m == 1:
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
    
    canvas = FigureCanvasTkAgg(plt.gcf(), master=page2)
    canvas.get_tk_widget().grid(column=0, row=1)
    plt.gcf().subplots(1, 2)
#     ani = FuncAnimation(plt.gcf(), animate, interval=10, blit=False)
        
#         canvas = FigureCanvasTkAgg(plt.gcf(), master=root1)
#         canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#         ani = FuncAnimation(plt.gcf(), animate, interval=10, blit=False)
#         plt.gcf().subplots(1, 2)
#         
#         toolbar = FigureCanvasTkAgg(canvas, root1)
#         toolbar.update()
#         canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#         
#         def _quit():
#             root1.quit()
#             root1.destroy()
#             
#         button = tk.Button(master=root1, text="Quit", command=_quit)
#         button.pack(side=tk.BOTTOM)
    
root = Tk()

style1 = font.Font(size = 25)

style2 = font.Font(size = 16)

page1 = Frame(root)
page2 = Frame(root)
page3 = Frame(root)

page1.grid(row=1, columns=1, sticky="nsew")
page2.grid(row=1, columns=1, sticky="nsew")
page3.grid(row=1, columns=1, sticky="nsew")

lb1 = Label(page1, text="Player Selections Page", font = style1)
lb1.pack(pady = 20)

lb2 = Label(page2, text="Graph Display Page", font = style1)
#lb2.pack(pady = 20)

lb3 = Label(page3, text="Final Conclusion", font = style1)
lb3.pack(pady = 20)

page1.tkraise()

btn1 = Button(page1, text = "Start Game", command=lambda: page2.tkraise(), font=style2)
btn1.pack()

btn2 = Button(page2, text = "Begin", command=go, font=style2)
btn2.grid(row=1, column=1)

# canvas = FigureCanvasTkAgg(plt.gcf(), master=page2)
# canvas.get_tk_widget().grid(column=0, row=1)
# plt.gcf().subplots(1, 2)

root.after(50000, root.destroy)
ani = FuncAnimation(plt.gcf(), animate, interval=10, blit=False)
root.mainloop()

# ts = 0.001
# cd = 0.002
# 
# fig1 = plt.figure()
# gs = fig1.add_gridspec(2, 2, hspace=0, wspace=0)
# (ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
# ax1.get_xaxis().set_visible(False)
# ax1.get_yaxis().set_visible(False)
# ax2.get_xaxis().set_visible(False)
# ax2.get_yaxis().set_visible(False)
# ax3.get_xaxis().set_visible(False)
# ax3.get_yaxis().set_visible(False)
# ax4.get_xaxis().set_visible(False)
# ax4.get_yaxis().set_visible(False)
# ax1.text(0.45, 0.45, '1', fontsize=32, fontweight='bold')
# ax2.text(0.45, 0.45, '2', fontsize=32, fontweight='bold')
# ax3.text(0.45, 0.45, '3', fontsize=32, fontweight='bold')
# ax4.text(0.45, 0.45, '4', fontsize=32, fontweight='bold')
# fig1.suptitle('Select your area of intent!')
# 
# plt.show(block=False)
# plt.pause(0.1)
# 
# num1 = int(input("Player 1 Choose an area of intent: "))
# num2 = int(input("Player 2 Choose an area of intent: "))
# 
# plt.close()
# 
# plt.ion()
# 
# x1 = list()
# y1 = list()
# x2 = list()
# y2 = list()
# 
# ser1 = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
# ser2 = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=1)
# 
# fig = plt.figure()
# gs = fig.add_gridspec(1, 2, hspace=0, wspace=0)
# (ax1, ax2) = gs.subplots(sharex='col', sharey='row')
# ax1.axis([0, 255, 0, 255])
# ax2.axis([0, 255, 0, 255])
# fig.suptitle('Random Coordinates')
# 
# if num1==1:
#         ax1.axvspan(0, 127, ymin=0.5, ymax=1, color='red', alpha=0.125)
#         ax1.axhspan(128, 255, xmin=0, xmax=0.5, color='red', alpha=0.125)
# if num1==2:
#         ax1.axvspan(128, 255, ymin=0.5, ymax=1, color='red', alpha=0.125)
#         ax1.axhspan(128, 255, xmin=0.5, xmax=1, color='red', alpha=0.125)
# if num1==3:
#         ax1.axvspan(0, 127, ymin=0, ymax=0.5, color='red', alpha=0.125)
#         ax1.axhspan(0, 127, xmin=0, xmax=0.5, color='red', alpha=0.125)
# if num1==4:
#         ax1.axvspan(128, 255, ymin=0, ymax=0.5, color='red', alpha=0.125)
#         ax1.axhspan(0, 127, xmin=0.5, xmax=1, color='red', alpha=0.125)
# 
# if num2==1:
#         ax2.axvspan(0, 127, ymin=0.5, ymax=1, color='blue', alpha=0.125)
#         ax2.axhspan(128, 255, xmin=0, xmax=0.5, color='blue', alpha=0.125)
# if num2==2:
#         ax2.axvspan(128, 255, ymin=0.5, ymax=1, color='blue', alpha=0.125)
#         ax2.axhspan(128, 255, xmin=0.5, xmax=1, color='blue', alpha=0.125)
# if num2==3:
#         ax2.axvspan(0, 127, ymin=0, ymax=0.5, color='blue', alpha=0.125)
#         ax2.axhspan(0, 127, xmin=0, xmax=0.5, color='blue', alpha=0.125)
# if num2==4:
#         ax2.axvspan(128, 255, ymin=0, ymax=0.5, color='blue', alpha=0.125)
#         ax2.axhspan(0, 127, xmin=0.5, xmax=1, color='blue', alpha=0.125)
# 
# n = 5
# while n > 0:
# 
#     output1 = ser1.read(1)
#     output2 = ser1.read(1)
#     output3 = ser2.read(1)
#     output4 = ser2.read(1)
# 
#     X1=int.from_bytes(output1,byteorder=sys.byteorder)
#     Y1=int.from_bytes(output2,byteorder=sys.byteorder)
#     X2=int.from_bytes(output3,byteorder=sys.byteorder)
#     Y2=int.from_bytes(output4,byteorder=sys.byteorder)
#     
#     x1.append(X1);
#     y1.append(Y1);
#     x2.append(X2);
#     y2.append(Y2);
# 
#     ax1.plot(x1, y1, 'or:')
#     ax2.plot(x2, y2, 'xb-')
# 
#     n -= 1
#     
#     plt.pause(0.01)
#     
#     if n == 0:
#         print("Game complete!")