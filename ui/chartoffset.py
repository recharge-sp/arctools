import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

from utils import chartoffset, tkevents

class ChartOffset(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.bind_class("Text","<Control-a>", tkevents.selectall)
        inputlabel = tk.Label(self, text="Input:").grid(column=0, row=0)
        self.inputnotes = scrolledtext.ScrolledText(self, width=50, height=5)
        self.inputnotes.grid(column=2, row=0)
        convert = tk.Button(self, text="Convert", command=self.convert)
        convert.grid(column=2, row=1)
        tk.Label(self, text="offset:").grid(column=0, row=1)
        self.offset = tk.Spinbox(self, from_=-(2<<64), to=2<<64, width=7)
        self.offset.grid(column=1, row=1)
        self.offset.delete("0", "end")
        self.offset.insert("0", "0")
        self.change_audio_offset = tk.BooleanVar(self)
        self.change_audio_offsetc = tk.Checkbutton(self, text="Change\n AudioOffset", variable=self.change_audio_offset)
        self.change_audio_offsetc.grid(column=0, row=2)
        tk.Label(self, text="Output:").grid(column=0, row=3)
        self.outputnotes = scrolledtext.ScrolledText(self, width=50, height=10)
        self.outputnotes.grid(column=2, row=3)
        self.pack()
    def convert(self):
        self.outputnotes.delete("1.0","end")
        for l in self.inputnotes.get("1.0","end").split("\n"):
            if len(l):
                self.outputnotes.insert("end", chartoffset.chartoffset(l, int(self.offset.get()), self.change_audio_offset.get()) + "\n")