from tkinter import *
import os
from PIL import Image, ImageTk

def LeftWing(tab, title, url, desc, address, time):

    buffer = Label(tab,
        text="",
        height = 2,
    )

    TitleName = Label(tab, 
        text="Title:",
        width = 20, 
        height = 1,
        fg = "white",
        bg = "black",
    )#.pack(side = "top")
    TitleName.pack(side = "top")

    buffer.pack(side = "top")

    Title = Label(tab, 
        text=title,
        width = 20, 
        height = 1,
    )#.pack(side = "top")
    Title.pack(side = "top")

    buffer.pack(side = "top")
    buffer.pack(side = "top")

    srcURLName = Label(tab, 
        text="Source URL:",
        width = 20, 
        height = 1,
        fg = "white",
        bg = "black",
    )#.pack(side = "top")
    srcURLName.pack(side = "top")

    buffer.pack(side = "top")

    srcURL = Label(tab, 
        text=url,
        width = 20, 
        height = 1,
    )#.pack(side = "top")
    srcURL.pack(side = "top")

    buffer.pack(side = "top")
    buffer.pack(side = "top")

    AddyName = Label(tab, 
        text="Address:",
        width = 20, 
        height = 1,
        fg = "white",
        bg = "black",
    )#.pack(side = "top")
    AddyName.pack(side = "top")

    buffer.pack(side = "top")

    Addy = Label(tab, 
        text=address,
        width = 80, 
        height = 1,
    )#.pack(side = "top")
    Addy.pack(side = "top")

    buffer.pack(side = "top")
    buffer.pack(side = "top")

    DescName = Label(tab, 
        text="Description:",
        width = 20, 
        height = 1,
        fg = "white",
        bg = "black",
    )#.pack(side = "top")
    DescName.pack(side = "top")

    buffer.pack(side = "top")

    Desc = Label(tab, 
        text=desc,
        width = 80, 
        height = 1,
    )#.pack(side = "top")
    Desc.pack(side = "top")

    buffer.pack(side = "top")
    buffer.pack(side = "top")

    TimeName = Label(tab, 
        text="Time",
        width = 20, 
        height = 1,
        fg = "white",
        bg = "black",
    )#.pack(side = "top")
    TimeName.pack(side = "top")

    buffer.pack(side = "top")

    Time = Label(tab, 
        text=url,
        width = 20, 
        height = 1,
    )#.pack(side = "top")
    Time.pack(side = "top")

    

    #tabWidget.place(relx=0.1, rely=0.1, anchor=NW)