import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

from utils import arcoffset, tkevents

class ArcOffset(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.bind_class("Text","<Control-a>", tkevents.selectall)
        inputlabel = tk.Label(self, text="Input:").grid(column=0, row=0)
        self.inputarcs = scrolledtext.ScrolledText(self, width=50, height=5)
        self.inputarcs.grid(column=4, row=0)
        convert = tk.Button(self, text="Convert", command=self.convert)
        convert.grid(column=4, row=1)
        tk.Label(self, text="dx:").grid(column=0, row=1)
        self.dx = tk.Spinbox(self, from_=-(2<<64), to=2<<64, increment=0.01, width=5)
        self.dx.grid(column=1, row=1)
        self.dx.delete("0", "end")
        self.dx.insert("0", "0.50")
        tk.Label(self, text="dy:").grid(column=0, row=2)
        self.dy = tk.Spinbox(self, from_=-(2<<64), to=2<<64, increment=0.01, width=5)
        self.dy.grid(column=1, row=2)
        self.dy.delete("0", "end")
        self.dy.insert("0", "0.50")
        tk.Label(self, text="Output:").grid(column=0, row=3)
        self.outputarc = scrolledtext.ScrolledText(self, width=50, height=10)
        self.outputarc.grid(column=4, row=3)
        self.pack()
    def convert(self):
        self.outputarc.delete("1.0","end")
        for l in self.inputarcs.get("1.0","end").split("\n"):
            if len(l):
                self.outputarc.insert("end", arcoffset.arcoffset(l, float(self.dx.get()), float(self.dy.get())))