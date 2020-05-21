import sys
import time
from tkinter import *

def tick():
    time_string = time.strftime("%I:%M:%S")
    date_string = time.strftime("%a, %b %d")
    clock.config(text=time_string)
    date.config(text=date_string)
    clock.after(200,tick)

gui = Tk()
gui.attributes('-fullscreen', True)
gui['bg']='gray'
# frames
topFrame = Frame(gui)
topFrame.pack(side=TOP)
bottomFrame = Frame(gui)
bottomFrame.pack(side=BOTTOM)

clock = Label(topFrame, font = ("times", 40, "bold"), bg="gray")
date = Label(bottomFrame, font = ("times", 40, "bold"), bg="gray")
clock.grid(row=0, column=1)
date.grid(row=0, column=1)
tick()
gui.mainloop()
