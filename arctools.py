import tkinter as tk
from tkinter import ttk

from ui.chartoffset import ChartOffset
from ui.arcoffset import ArcOffset
from ui.splitarc import SplitArc
from ui.easedtimings import EasedTimings

root = tk.Tk()
root.title("arctools")
notebook = ttk.Notebook(root)
chartoffset = ChartOffset(notebook)
notebook.add(chartoffset, text="Chart offset")
arcoffset = ArcOffset(notebook)
notebook.add(arcoffset, text="Arc offset")
splitarc = SplitArc(notebook)
notebook.add(splitarc, text="Split arc")
easedtimings = EasedTimings(notebook)
notebook.add(easedtimings, text="Eased timings")
notebook.pack()
root.resizable(False, False)
tk.mainloop()