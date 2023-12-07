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

class GraphPage():
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
    
    def graph_window():
        
        
        root = tk.Tk()
        root.wm_title("Embedding in Tk")
        
        f = Figure(figsize=(5,4), dpi=100)
        a = f.add_subplot(111)
       

        
        def animate(i):
            c1 = app.cursor
            c1.execute("SELECT time FROM data ORDER BY time DESC LIMIT 1")
            
            x1 = list()
            y1 = list()
            x2 = list()
            y2 = list()

            ser1 = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
            ser2 = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=1)
           
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

            Xaxes = [x1]
            Yaxes = [y1]
        
            pltYaxes = np.array(Yaxes)
            pltXaxes = np.array(Xaxes)

            a.clear()
            a.plot(pltXaxes,pltYaxes)
            
        
        canvas = FigureCanvasTkAgg(f, master=root)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        
        def _quit():
            root.quit()     
            root.destroy()
            
        button = tk.Button(master=root, text="Quit", command=_quit)
        button.pack(side=tk.BOTTOM)
        root.ani = animation.FuncAnimation(f,animate, interval=5000)

        root.geometry("800x480+0+0")
        root.attributes("-fullscreen", True)
        root.mainloop()
    
app = GraphPage()
app.mainloop()