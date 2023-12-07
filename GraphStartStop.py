try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import serial, sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib.animation as animation

import random

x1 = list()
y1 = list()
x2 = list()
y2 = list()

# ser1 = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
# ser2 = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=1)

# output1 = ser1.read(1)
# output2 = ser1.read(1)
# output3 = ser2.read(1)
# output4 = ser2.read(1)

num1 = int(input("Player 1 Choose an area of intent: "))
num2 = int(input("Player 2 Choose an area of intent: "))

def get_data():
    while True:
    
        ser1 = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)
        ser2 = serial.Serial('/dev/ttyACM1', 9600, 8, 'N', 1, timeout=1)
#     
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
        
        return x1, y1, x2, y2

class App(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        self.running = False
        self.ani = None

        btns = tk.Frame(self)
        btns.pack()

        lbl = tk.Label(btns, text="Number of times to run")
        lbl.pack(side=tk.LEFT)

        self.points_ent = tk.Entry(btns, width=5)
        self.points_ent.insert(0, '50')
        self.points_ent.pack(side=tk.LEFT)

        lbl = tk.Label(btns, text="update interval (ms)")
        lbl.pack(side=tk.LEFT)

        self.interval = tk.Entry(btns, width=5)
        self.interval.insert(0, '100')
        self.interval.pack(side=tk.LEFT)

        self.btn = tk.Button(btns, text='Start', command=self.on_click)
        self.btn.pack(side=tk.LEFT)

        self.fig = plt.Figure()
        self.ax1, ax2, = plt.gcf().get_axes()
        
        self.ax1.cla()
        self.ax2.cla()
        
#         self.ax2 = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        self.ax1.axis([0, 255, 0, 255])
        self.ax2.axis([0, 255, 0, 255])

#         self.ax1.set_ylim(0,255)
#         self.ax1.set_xlim(0,255)
#         self.ax2.set_ylim(0,255)
#         self.ax2.set_xlim(0,255)

    def on_click(self):
        '''the button is a start, pause and unpause button all in one
        this method sorts out which of those actions to take'''
        if self.ani is None:
            # animation is not running; start it
            return self.start()

        if self.running:
            # animation is running; pause it
            self.ani.event_source.stop()
            self.btn.config(text='Un-Pause')
        else:
            # animation is paused; unpause it
            self.ani.event_source.start()
            self.btn.config(text='Pause')
        self.running = not self.running

    def start(self):
        self.points = int(self.points_ent.get()) + 1
        self.ani = animation.FuncAnimation(
            self.fig,
            self.update_graph,
            frames=self.points,
            interval=int(self.interval.get()),
            repeat=False)
        self.running = True
        self.btn.config(text='Pause')
        self.ani._start()
        print('started animation')

    def update_graph(self, i):
        self.line.set_data(*get_data()) # update graph

        if i >= self.points - 1:
            # code to limit the number of run times; could be left out
            self.btn.config(text='Start')
            self.running = False
            self.ani = None
        return self.line,

def main():
    root = tk.Tk()
    app = App(root)
    app.pack()
    root.mainloop()

if __name__ == '__main__':
    main()