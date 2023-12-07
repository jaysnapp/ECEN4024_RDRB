#Random De-Random Bot

import serial, sys
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font
from tkinter import Frame
from itertools import count
import random
from matplotlib import style


LARGE_FONT = ("Verdana", 12)
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
    

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
#         tk.Tk.iconbitmap(self, default="clienticon.ico")
#         tk.Tk.wm_title(self, "Random DeRandom Bot")

#         self.rowconfigure(0, weight=1)
#         self.columnconfigure(0, weight=1)
#         
#         self.screens = {}
#         
#         for screen in (PlayerSelect, Player1Selection, Player2Selection, GamePage2, WinLosePage):
#             self.screens[screen] = screen(self)
#             self.screens[screen].grid(row=0, column=0, sticky="nsew")
#             
#     def show_screen(self, screen):
#         target = self.screens[screen]
#         
#         if screen is PlayerSelect: target.update_label()
#         
#         target.tkraise()
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (PlayerSelect, Player1Selection, Player2Selection, GamePage2, WinLosePage):
#         for F in (PlayerSelect, Player1Consent, Player2Consent, Player1Info, Player2Info, Player1Selection, Player2Selection, GamePage1, GamePage2, WinLosePage):
        
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(PlayerSelect)
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
        
class PlayerSelect(tk.Frame):
    
    def ___init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Player Select", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(self, text="1 Player", command=lambda: controller.show_screen(Player1Selection))
        button.pack()
        
        button2 = ttk.Button(self, text="2 Players", command=lambda: controller.show_screen(Player1Selection))
        button2.pack()
        
        
class Player1Selection(tk.Frame):
    
    def ___init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Player 1 Info", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Next", command=lambda: controller.show_screen(Player2Selection))
        button1.pack()
        
class Player2Selection(tk.Frame):
    
    def ___init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Player 1 Info", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Next", command=lambda: controller.show_screen(GamePage2))
        button1.pack()
        
class GamePage2(tk.Frame):
    
    def ___init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Player 1 Info", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="End Game", command=lambda: controller.show_screen(WinLosePage))
        button1.pack()
        
        canvas = FigureCanvasTkAgg(plt.gcf(), master=GamePage2)
        canvas.get_tk_widget().grid(column=0, row=1)
        plt.gcf().subplots(1, 2)
#         ani = FuncAnimation(plt.gcf(), animate, interval=10, blit=False)
        
class WinLosePage(tk.Frame):
    
    def ___init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="You either won or lost IDK", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="End Game", command=lambda: controller.show_screen(PlayerSelect))
        button1.pack()
        
app = App()
ani = FuncAnimation(plt.gcf(), animate, interval=10, blit=False)
app.mainloop()