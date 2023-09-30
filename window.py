from tkinter import *
from tkinter import ttk

import maps
#import leftTab


win = Tk()
win.geometry(f"{1000}x{750}")
win.title("UCrisis")

# Create a notebook that holds the tabs
notebook = ttk.Notebook(win)

# Create tab frames
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Add the tab frames to the notebook
notebook.add(tab1, text="Map")
notebook.add(tab2, text="User Information")

notebook.pack(expand=1, fill='both')

# Place widgets in tab1
#map_widget.place(relx=1, rely=0, anchor=tkinter.NE)
maps.tabbed_window(tab1)


# Place widgets in tab2
Label(tab2, text="Type your location:").pack()
Entry(tab2, width=100).pack()
#leftTab.submit(tab2)

win.mainloop()