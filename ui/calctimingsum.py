import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

from utils import calctimingsum, tkevents

class TimingSum(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.bind_class("Text","<Control-a>", tkevents.selectall)
        inputlabel = tk.Label(self, text="Input:").grid(column=0, row=0)
        self.inputnotes = scrolledtext.ScrolledText(self, width=50, height=5)
        self.inputnotes.grid(column=2, row=0)
        convert = tk.Button(self, text="Calculate", command=self.calculate)
        convert.grid(column=2, row=1)
        tk.Label(self, text="Base BPM:").grid(column=0, row=1)
        self.basebpm = tk.Spinbox(self, from_=-(2<<64), to=2<<64, increment=0.01, width=7)
        self.basebpm.grid(column=1, row=1)
        self.basebpm.delete("0", "end")
        self.basebpm.insert("0", "100.00")
        tk.Label(self, text="Output:").grid(column=0, row=2)
        self.outputnotes = scrolledtext.ScrolledText(self, width=50, height=10)
        self.outputnotes.grid(column=2, row=3)
        self.pack()
    def calculate(self):
        self.outputnotes.delete("1.0","end")
        timings = self.inputnotes.get("1.0","end").split("\n")
        self.outputnotes.insert("end", calctimingsum.calctimingsum(float(self.basebpm.get()), timings))
