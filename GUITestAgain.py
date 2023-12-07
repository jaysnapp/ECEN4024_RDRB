import serial
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk


LARGE_FONT= ("Verdana", 12)
plt.style.use('fivethirtyeight')

# f = Figure(figsize=(5,5), dpi=100)
# a = f.add_subplot(111)

ser1 = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
ser2 = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=1)

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

# def animate(i):
#     pullData = open("sampleText.txt","r").read()
#     dataList = pullData.split('\n')
#     xList = []
#     yList = []
#     for eachLine in dataList:
#         if len(eachLine) > 1:
#             x, y = eachLine.split(',')
#             xList.append(int(x))
#             yList.append(int(y))
# 
#     a.clear()
#     a.plot(xList, yList)

    
            

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

#         tk.Tk.iconbitmap(self, default="clienticon.ico")
#         tk.Tk.wm_title(self, "Sea of BTC client")
        
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph Page",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        
        canvas = FigureCanvasTkAgg(plt.gcf(), master=Page1)
        canvas.get_tk_widget().grid(column=0, row=1)
        plt.gcf().subplots(1, 2)
        

#         canvas = FigureCanvasTkAgg(f, self)
#         canvas.show()
#         canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
# 
#         toolbar = NavigationToolbar2Tk(canvas, self)
#         toolbar.update()
#         canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
# ani = animation.FuncAnimation(f, animate, interval=1000)
ani = FuncAnimation(plt.gcf(), animate, interval=10, blit=False)
app.mainloop()