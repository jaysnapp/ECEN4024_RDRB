import serial, sys
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from itertools import count
import random
from matplotlib import style
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font
from tkinter import Frame


LARGEFONT =("Verdana", 35)

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

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {} 

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with 
			# for loop
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
		
		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

		


# second window frame page1 
class Page1(tk.Frame):
	
	def __init__(self):
		super(Page1, self).__init__()
		self.widgets={}
		self.grid(column=0, row=1)
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Page 2",
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by 
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)
canvas = FigureCanvasTkAgg(plt.gcf(), master=Page1)
canvas.get_tk_widget().grid(column=0, row=1)
plt.gcf().subplots(1, 2)


# third window frame page2
class Page2(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Page 1",
							command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by 
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
ani = FuncAnimation(plt.gcf(), animate, interval=10, blit=False)
app.mainloop()
