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

global num1, num2, x, y, a, b, c, s, x11, x22

plt.style.use('default')

LARGEFONT =("Verdana", 50)

LF = ("Verdana", 20, 'bold')

MF = ("Verdana", 16)

x1 = []
y1 = []
x2 = []
y2 = []

a = int
c = int
j = int
s = int
t = str()
t1 = str()
x = int
y = int
z = int
num1 = int
num2 = int

j1 = []
j2 = []
j3 = []
j4 = []

x11 = []
x22 = []

f = Figure(figsize=(16,9), dpi=100)
f1 = f.add_subplot(131)
f2 = f.add_subplot(133)

class tkinterApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        container.grid(column=0, row=0, sticky='nsew')
        
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        
        for F in (StartPage, Page1, Page1a, Page2, Page3, Page4):
            
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky="nsew")
            
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def Single_Player(self, cont):
        global x
        frame = self.frames[cont]
        frame.tkraise()
        x = 1
        
    def Multiplayer(self, cont):
        global x
        frame = self.frames[cont]
        frame.tkraise()
        x = 2
        
    def StartGraph(self, cont):
        global a, b, j, y, z, s
        frame = self.frames[cont]
        frame.tkraise()
        b = 0
        a = 0
        j = 0
        y = 1
        z = 0
        s = 0
        
    def PauseAni(self, cont):
        global a, fig, t, x1, y1, x2, y2, x11, x22, j1, j2, j3, j4, t1
        frame = self.frames[cont]
        frame.tkraise()
        a = 1
        if num1 == 1:
            for x, y in zip(x1, y1):
                x11.append([x,y])
            j1 = sorted(x for x in x11 if x[0] < 128)
            j2 = sorted(y for y in j1 if y[1] > 127)
        
        if num1 == 2:
            for x, y in zip(x1, y1):
                x11.append([x,y])
            j1 = sorted(x for x in x11 if x[0] > 127)
            j2 = sorted(y for y in j1 if y[1] > 127)
        
        if num1 == 3:
            for x, y in zip(x1, y1):
                x11.append([x,y])
            j1 = sorted(x for x in x11 if x[0] < 128)
            j2 = sorted(y for y in j1 if y[1] < 128)
        
        if num1 == 4:
            for x, y in zip(x1, y1):
                x11.append([x,y])
            j1 = sorted(x for x in x11 if x[0] > 127)
            j2 = sorted(y for y in j1 if y[1] < 128)
        t = len(j2)
        
        if num2 == 1:
            for x, y in zip(x2, y2):
                x22.append([x,y])
            j3 = sorted(x for x in x22 if x[0] < 128)
            j4 = sorted(y for y in j3 if y[1] > 127)
        
        if num2 == 2:
            for x, y in zip(x2, y2):
                x22.append([x,y])
            j3 = sorted(x for x in x22 if x[0] > 127)
            j4 = sorted(y for y in j3 if y[1] > 127)
        
        if num2 == 3:
            for x, y in zip(x2, y2):
                x22.append([x,y])
            j3 = sorted(x for x in x22 if x[0] < 128)
            j4 = sorted(y for y in j3 if y[1] < 128)
        
        if num2 == 4:
            for x, y in zip(x2, y2):
                x22.append([x,y])
            j3 = sorted(x for x in x22 if x[0] > 127)
            j4 = sorted(y for y in j3 if y[1] < 128)
        t1 = len(j4)
        
    def ResetGraph(self, cont):
        global s, z, x1, y1, x2, y2, s, x11, x22, t, t1, j1, j2, j3, j4, int_var, int_var1
        x1.clear()
        y1.clear()
        x2.clear()
        y2.clear()
        x11.clear()
        x22.clear()
        j1.clear()
        j2.clear()
        j3.clear()
        j4.clear()
        int_var.set(0)
        int_var1.set(0)
        s = 0
        frame = self.frames[cont]
        frame.tkraise()
        z = 1
        t = 0
        t1 = 0
      
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text = "Start Game", font = LARGEFONT)
        
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
        
        button1 = tk.Button(self, text="Single Player",
        command = lambda: controller.Single_Player(Page1), background= "Red", height=26, width=37, font=LF)
        
        button1.grid(row = 1, column = 1, padx = 9, pady = 10)
        
        button2 = tk.Button(self, text="Multiplayer",
        command = lambda: controller.Multiplayer(Page1a), background = "Purple", height=26, width=37, font=LF, fg = "White")
        
        button2.grid(row = 1, column = 3, padx = 10, pady = 10)

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text = "Player 1 Choose Your Area of Intent!", font = ("Verdana", 30, 'bold'))
        
        label.grid(row = 0, column = 2, padx = 10, pady = 50)
        
        button1 = tk.Button(self, text="Start Game",
        command = lambda: controller.StartGraph(Page3), background = "Red", font = ("Verdana", 16, 'bold'))
         
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)
        
        listbox = Listbox(master = self, height=5,
                          width = 10,
                          selectmode = SINGLE,
                          bg = "grey",
                          activestyle = 'dotbox',
                          font = ("Verdana", 18, 'bold'),
                          fg = "Red")
        
        listbox.insert(1, 1)
        listbox.insert(2, 2)
        listbox.insert(3, 3)
        listbox.insert(4, 4)
        
        listbox.grid(row = 2, column = 2)
        
        label1 = ttk.Label(self, text = "Select a number from the list," '\n'
                           "click Choose Number," '\n'
                           "then click Start Game!", font = ("Verdana", 20, 'bold'))
        
        label1.grid(row = 3, column = 2, padx = 10, pady = 10)

        def selected_item():
            global num1
            for i in listbox.curselection():
                a = listbox.get(i)
                if a == 1:
                    num1 = 1
                if a == 2:
                    num1 = 2
                if a == 3:
                    num1 = 3
                if a == 4:
                    num1 = 4
        
        button3 = tk.Button(self, text="Choose Number",
        command = selected_item, background="Red", font = ("Verdana", 16, 'bold'))
        
        button3.grid(row = 2, column = 1, padx = 100, pady = 100)
        
        image = Image.open("AreaofIntent.png")
        photo = ImageTk.PhotoImage(image.resize((500, 500), Image.ANTIALIAS))
        
        label2 = ttk.Label(self, image=photo)
        label2.image = photo
        label2.grid(row = 2, column = 3, pady=100)
        
class Page1a(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text = "Player 1 Choose Your Area of Intent!", font = ("Verdana", 30, 'bold'))
        
        label.grid(row = 0, column = 2, padx = 10, pady = 50)
        
        button1 = tk.Button(self, text="Player 2",
        command = lambda: controller.show_frame(Page2), background = "Blue", font = ("Verdana", 16, 'bold'), fg = "White")
         
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)
        
        listbox = Listbox(master = self, height=5,
                          width = 10,
                          selectmode = SINGLE,
                          bg = "grey",
                          activestyle = 'dotbox',
                          font = ("Verdana", 18, 'bold'),
                          fg = "Red")
        
        listbox.insert(1, 1)
        listbox.insert(2, 2)
        listbox.insert(3, 3)
        listbox.insert(4, 4)
        
        listbox.grid(row = 2, column = 2)
        
        label1 = ttk.Label(self, text = "Select a number from the list," '\n'
                           "click Choose Number," '\n'
                           "then let Player 2 choose!", font = ("Verdana", 20, 'bold'))
        
        label1.grid(row = 3, column = 2, padx = 10, pady = 10)

        def selected_item():
            global num1
            for i in listbox.curselection():
                a = listbox.get(i)
                if a == 1:
                    num1 = 1
                if a == 2:
                    num1 = 2
                if a == 3:
                    num1 = 3
                if a == 4:
                    num1 = 4
        
        button3 = tk.Button(self, text="Choose Number",
        command = selected_item, background="Red", font = ("Verdana", 16, 'bold'))
        
        button3.grid(row = 2, column = 1, padx = 100, pady = 100)
        
        image = Image.open("AreaofIntent.png")
        photo = ImageTk.PhotoImage(image.resize((500, 500), Image.ANTIALIAS))
        
        label2 = ttk.Label(self, image=photo)
        label2.image = photo
        label2.grid(row = 2, column = 3, pady=100)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text = "Player 2 Choose Your Area of Intent!", font = ("Verdana", 30, 'bold'))
        
        label.grid(row = 0, column = 2, padx = 10, pady = 50)
        
        button1 = tk.Button(self, text="Start Game",
        command = lambda: controller.StartGraph(Page3), background = "Blue", font = ("Verdana", 16, 'bold'), fg = "White")
         
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)
        
        listbox = Listbox(master = self, height=5,
                          width = 10,
                          selectmode = SINGLE,
                          bg = "grey",
                          activestyle = 'dotbox',
                          font = ("Verdana", 18, 'bold'),
                          fg = "Blue")
        
        listbox.insert(1, 1)
        listbox.insert(2, 2)
        listbox.insert(3, 3)
        listbox.insert(4, 4)
        
        listbox.grid(row = 2, column = 2)
        
        label1 = ttk.Label(self, text = "Select a number from the list," '\n'
                           "click Choose Number," '\n'
                           "then click Start Game!", font = ("Verdana", 20, 'bold'))
        
        label1.grid(row = 3, column = 2, padx = 10, pady = 10)

        def selected_item():
            global num2
            for i in listbox.curselection():
                a = listbox.get(i)
                if a == 1:
                    num2 = 1
                if a == 2:
                    num2 = 2
                if a == 3:
                    num2 = 3
                if a == 4:
                    num2 = 4
        
        button3 = tk.Button(self, text="Choose Number",
        command = selected_item, background="Blue", font = ("Verdana", 16, 'bold'), fg = "White")
        
        button3.grid(row = 2, column = 1, padx = 100, pady = 100)
        
        image = Image.open("AreaofIntent.png")
        photo = ImageTk.PhotoImage(image.resize((500, 500), Image.ANTIALIAS))
        
        label2 = ttk.Label(self, image=photo)
        label2.image = photo
        label2.grid(row = 2, column = 3, pady=100)

def animate(i):
    global j, num1, num2, x, x1, x2, y, y1, y2, z, s, x11, x22
    if y == 1:
        if j < 30:
            if x == 1:
                if z == 0:
                
                    ser1 = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
                    ser2 = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=1)
                
                    output1 = ser1.read(1)
                    output2 = ser1.read(1)
                    
                    X1=int.from_bytes(output1,byteorder=sys.byteorder)
                    Y1=int.from_bytes(output2,byteorder=sys.byteorder)
                    
                    x1.append(X1);
                    y1.append(Y1);
                
                f1.cla()
                f2.cla()
                
                f1.axis([0, 255, 0, 255])
                f2.axis([0, 255, 0, 255])
                
                if num1==1:
                    f1.axvspan(0, 127, ymin=0.5, ymax=1, color='red', alpha=0.125)
                    f1.axhspan(128, 255, xmin=0, xmax=0.5, color='red', alpha=0.125)
                if num1==2:
                    f1.axvspan(128, 255, ymin=0.5, ymax=1, color='red', alpha=0.125)
                    f1.axhspan(128, 255, xmin=0.5, xmax=1, color='red', alpha=0.125)
                if num1==3:
                    f1.axvspan(0, 127, ymin=0, ymax=0.5, color='red', alpha=0.125)
                    f1.axhspan(0, 127, xmin=0, xmax=0.5, color='red', alpha=0.125)
                if num1==4:
                    f1.axvspan(128, 255, ymin=0, ymax=0.5, color='red', alpha=0.125)
                    f1.axhspan(0, 127, xmin=0.5, xmax=1, color='red', alpha=0.125)
                
                f1.plot(x1, y1, 'or:')
                
            elif x == 2:
                if z == 0:
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

                f1.cla()
                f2.cla()

                f1.axis([0, 255, 0, 255])
                f2.axis([0, 255, 0, 255])
                
                if num1==1:
                    f1.axvspan(0, 127, ymin=0.5, ymax=1, color='red', alpha=0.125)
                    f1.axhspan(128, 255, xmin=0, xmax=0.5, color='red', alpha=0.125)
                    
                if num1==2:
                    f1.axvspan(128, 255, ymin=0.5, ymax=1, color='red', alpha=0.125)
                    f1.axhspan(128, 255, xmin=0.5, xmax=1, color='red', alpha=0.125)
                if num1==3:
                    f1.axvspan(0, 127, ymin=0, ymax=0.5, color='red', alpha=0.125)
                    f1.axhspan(0, 127, xmin=0, xmax=0.5, color='red', alpha=0.125)
                if num1==4:
                    f1.axvspan(128, 255, ymin=0, ymax=0.5, color='red', alpha=0.125)
                    f1.axhspan(0, 127, xmin=0.5, xmax=1, color='red', alpha=0.125)

                if num2==1:
                    f2.axvspan(0, 127, ymin=0.5, ymax=1, color='blue', alpha=0.125)
                    f2.axhspan(128, 255, xmin=0, xmax=0.5, color='blue', alpha=0.125)
                if num2==2:
                    f2.axvspan(128, 255, ymin=0.5, ymax=1, color='blue', alpha=0.125)
                    f2.axhspan(128, 255, xmin=0.5, xmax=1, color='blue', alpha=0.125)
                if num2==3:
                    f2.axvspan(0, 127, ymin=0, ymax=0.5, color='blue', alpha=0.125)
                    f2.axhspan(0, 127, xmin=0, xmax=0.5, color='blue', alpha=0.125)
                if num2==4:
                    f2.axvspan(128, 255, ymin=0, ymax=0.5, color='blue', alpha=0.125)
                    f2.axhspan(0, 127, xmin=0.5, xmax=1, color='blue', alpha=0.125)
                
                f1.plot(x1, y1, 'or:')
                f2.plot(x2, y2, 'xb-')
                
        j += 1

class Page3(tk.Frame):
    global j, s
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        
        canvas = FigureCanvasTkAgg(f, master=self)
        canvas.get_tk_widget().grid(padx = 150, pady=20)
        
        button2 = tk.Button(self, text="Please wait until graph is finished and then press this button to proceed",
        command = lambda: controller.PauseAni(Page4), font = ("Verdana", 16, 'bold'), bg="Purple", fg="White", height=5, width=100)
        
        button2.grid(padx = 10, pady = 1)

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        
        global int_var, int_var1
        
        def results():
            global t, t1, int_var, int_var1
            int_var.set(int(t))
            int_var1.set(int(t1))
            
        int_var = IntVar()
        int_var1 = IntVar()
        
        int_var.set(0)
        int_var1.set(0)
        
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text = "Results Page", font = LARGEFONT)
        
        label.grid(row = 0, column = 1)
        
        button1 = tk.Button(self, text="New Game",
        command = lambda: controller.ResetGraph(StartPage), font = MF, bg = "Orange", fg = "Black", height = 5, width = 20)
        
        button1.grid(row = 5, column = 1, padx = 200, pady = 10)
        
        label1 = tk.Label(self, text = "Player 1", font = LARGEFONT)
        label1.grid(row = 1, column = 0, padx = 20, pady = 50)
        
        label2 = tk.Label(self, text = "Player 2", font = LARGEFONT)
        label2.grid(row = 1, column = 2, padx = 10, pady = 50)
        
        status = tk.Label(self, textvariable = int_var , font = LARGEFONT)
        status.grid(row = 2, column = 0, padx = 10, pady = 50)
        
        status1 = tk.Label(self, textvariable = int_var1 , font = LARGEFONT)
        status1.grid(row = 2, column = 2, padx = 10, pady = 50)
        
        label1 = tk.Label(self, text = "Out of 30 points", font = LARGEFONT)
        label1.grid(row = 3, column = 0, padx = 25, pady = 50)
        
        label2 = tk.Label(self, text = "Out of 30 points", font = LARGEFONT)
        label2.grid(row = 3, column = 2, padx = 10, pady = 50)
        
        button3 = tk.Button(self, text="Click me to see how you did!",
        command = results, bg="Orange", fg="Black", font = MF, height = 5, width = 22)
        
        button3.grid(row = 4, column = 1, padx = 10, pady = 10)

        
app = tkinterApp()
ani = FuncAnimation(f, animate, interval=300, blit=False)

if a == 0:
    ani.resume()
if a == 1:
    ani.pause()

app.attributes('-fullscreen', True)
app.mainloop()