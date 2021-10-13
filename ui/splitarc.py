import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

from utils import splitarc, tkevents

class SplitArc(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.bind_class("Text","<Control-a>", tkevents.selectall)
        inputlabel = tk.Label(self, text="Input:").grid(column=0, row=0)
        self.inputarcs = scrolledtext.ScrolledText(self, width=50, height=5)
        self.inputarcs.grid(column=4, row=0)
        convert = tk.Button(self, text="Convert", command=self.convert)
        convert.grid(column=4, row=1)
        self.fliparc = tk.BooleanVar(self)
        self.fliparcc = tk.Checkbutton(self, text="Flip between\n arc and traces", variable=self.fliparc)
        self.fliparcc.grid(column=0, row=1)
        tk.Label(self, text="Parts:").grid(column=0, row=2)
        self.parts = tk.Spinbox(self, from_=2, to=64, width=5)
        self.parts.grid(column=1, row=2)
        self.parts.delete("0", "end")
        self.parts.insert("0", "8")
        tk.Label(self, text="Output:").grid(column=0, row=3)
        self.outputarc = scrolledtext.ScrolledText(self, width=50, height=10)
        self.outputarc.grid(column=4, row=3)
        self.pack()
    def convert(self):
        self.outputarc.delete("1.0","end")
        for l in self.inputarcs.get("1.0","end").split("\n"):
            if len(l):
                self.outputarc.insert("end", splitarc.splitarc(l, int(self.parts.get()), self.fliparc.get()))