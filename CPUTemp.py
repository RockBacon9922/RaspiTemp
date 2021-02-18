try:
    import Tkinter as tk
except:
    import tkinter as tk
import time
from gpiozero import CPUTemperature
cpu = CPUTemperature()

class temp():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CPUTemperature")
        self.label = tk.Label(text="", font=('Helvetica', 48), fg='red')
        self.label.pack()
        self.label3 = tk.Label(text="In Celcius", font=('Helvetica', 20), fg='green')
        self.label3.pack()
        self.label2 = tk.Label(text="By William Stoneham", font=('Helvetica', 20), fg='orange')
        self.label2.pack()
        self.update_clock()
        self.root.mainloop()
    def update_clock(self):
        now = str(cpu.temperature)
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)
app=temp()
