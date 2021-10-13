import tkinter as tk
from tkinter import ttk

from ui.splitarc import SplitArc
from ui.easedtimings import EasedTimings

root = tk.Tk()
root.title("arctools")
notebook = ttk.Notebook(root)
splitarc = SplitArc(notebook)
notebook.add(splitarc, text="Split arc")
easedtimings = EasedTimings(notebook)
notebook.add(easedtimings, text="Eased timings")
notebook.pack()
tk.mainloop()