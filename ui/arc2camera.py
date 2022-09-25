import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

from utils import arc2camera, tkevents

hint = """blue arc: x, y -> transverse, bottomzoom
red arc: x, y -> angle, linezoon
green arc: x, y -> steadyangle, topzoom"""

class Arc2Camera(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.bind_class("Text","<Control-a>", tkevents.selectall)
        inputlabel = tk.Label(self, text="Input:").grid(column=0, row=0)
        self.inputnotes = scrolledtext.ScrolledText(self, width=50, height=5)
        self.inputnotes.grid(column=2, row=0)
        convert = tk.Button(self, text="Convert", command=self.convert)
        convert.grid(column=2, row=1)
        tk.Label(self, text=hint).grid(column=1, row=1)
        tk.Label(self, text="Output:").grid(column=0, row=2)
        self.outputnotes = scrolledtext.ScrolledText(self, width=50, height=10)
        self.outputnotes.grid(column=2, row=2)
        self.pack()
    def convert(self):
        self.outputnotes.delete("1.0","end")
        # transverse, bottomzoom, linezoom, steadyangle, topzoom, angle
        for l in self.inputnotes.get("1.0","end").split("\n"):
            if len(l):
                self.outputnotes.insert("end", arc2camera.arc2camera(l) + "\n")
