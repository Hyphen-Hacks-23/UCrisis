from tkinter import *
import os
from PIL import Image, ImageTk

def LeftWing(tab, title, url, desc, address, time):

    buffer = Label(tab,
        text="",
        height = 2,
    )

    srcURLName = Label(tab, 
        text="Source URL:",
        width = 20, 
        height = 1,
        fg = "white",
        bg = "black",
    )#.pack(side = "left")
    srcURLName.pack(side = "left")

    buffer.pack(side = "left")

    srcURL = Label(tab, 
        text=url,
        width = 20, 
        height = 1,
    )#.pack(side = "left")
    srcURL.pack(side = "left")

    buffer.pack(side = "left")
    buffer.pack(side = "left")

    AddyName = Label(tab, 
        text="Address:",
        width = 20, 
        height = 1,
        fg = "white",
        bg = "black",
    )#.pack(side = "left")
    AddyName.pack(side = "left")

    buffer.pack(side = "left")

    Addy = Label(tab, 
        text=address,
        width = 80, 
        height = 1,
    )#.pack(side = "left")
    Addy.pack(side = "left")

    buffer.pack(side = "left")
    buffer.pack(side = "left")

    DescName = Label(tab, 
        text="Description:",
        width = 20, 
        height = 1,
        fg = "white",
        bg = "black",
    )#.pack(side = "left")
    DescName.pack(side = "left")

    buffer.pack(side = "left")

    Desc = Label(tab, 
        text=desc,
        width = 80, 
        height = 1,
    )#.pack(side = "left")
    Desc.pack(side = "left")

    

    #tabWidget.place(relx=0.1, rely=0.1, anchor=NW)