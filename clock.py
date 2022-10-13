# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Clock')
root.resizable()
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
lbl = Label(root, font = ('calibri', 40, 'bold'),background = 'black',foreground = 'white')

lbl.pack()

time()

mainloop()
