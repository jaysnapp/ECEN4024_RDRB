import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import serial, string, sys, time
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

x1a = list()
y1a = list()
x2a = list()
y2a = list()

plt.style.use('default')



# 
# if a == 1:
#             fig = Figure(figsize=(5,5), dpi = 100)
#             global b, j, x, y, z, x1a, x2a, y1a, y2a
#             if y == 1:
#                 if j < 20:
#                     if x == 1:
#                         if z == 0:
#                 
#                             fig, axs = plt.subplots(1, 2)
#                             
#                             axs.cla()
#                             
#                             axs[0,0].plot(x1a, y1a, 'or:')
#                             axs[0,0].set_title("P1 x and y correlation")
#                             axs[0,1].plot(x1a, x2a, 'or:')
#                             axs[0,1].set_title("P1 and P2 correlation")
#                             
#                     elif x == 2:
#                         if z == 0:
# 
#                             fig, axs = plt.subplots(1, 3)
#                             
#                             axs.cla()
#                             
#                             axs[0,0].plot(x1a, y1a, 'or:')
#                             axs[0,0].set_title("P1 x and y correlation")
#                             axs[0,1].plot(x1a, x2a, 'or:')
#                             axs[0,1].set_title("P1 and P2 correlation")
#                             axs[0,2].plot(x2a, y2a, 'or:')
#                             axs[0,2].set_title("P2 x and y correlation")
#                 j += 1
#             
#             canvas1 = FigureCanvasTkAgg(fig, master=self)
#             canvas1.draw()