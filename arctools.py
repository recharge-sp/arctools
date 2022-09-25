#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

from ui.chartoffset import ChartOffset
from ui.arcoffset import ArcOffset
from ui.splitarc import SplitArc
from ui.easedtimings import EasedTimings
from ui.arc2camera import Arc2Camera
from ui.calctimingsum import TimingSum

root = tk.Tk()
root.title("arctools")
style = ttk.Style(root)
style.configure("lefttab.TNotebook", tabposition="wn")
notebook = ttk.Notebook(root, style="lefttab.TNotebook")
chartoffset = ChartOffset(notebook)
notebook.add(chartoffset, text="Chart offset")
arcoffset = ArcOffset(notebook)
notebook.add(arcoffset, text="Arc offset")
splitarc = SplitArc(notebook)
notebook.add(splitarc, text="Split arc")
camera = Arc2Camera(notebook)
notebook.add(camera, text="Arc to camera")
easedtimings = EasedTimings(notebook)
notebook.add(easedtimings, text="Eased timings")
notebook.pack()
timingsum = TimingSum(notebook)
notebook.add(timingsum, text="Timing Sum")
notebook.pack()
root.resizable(False, False)
tk.mainloop()