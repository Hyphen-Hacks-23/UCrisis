from tkinter import *
import os
from PIL import Image, ImageTk

def LeftWing_init(tab):

    TitleName = Label(tab, 
        text="Title:",
        width = 20, 
        height = 1,
        fg = "white",
        bg = f"#333333",
        wraplength=200
    )
    TitleName.pack(side = "top", padx=10, pady = (10,0), anchor="e")

    global Title
    Title = Label(tab, 
        text="title",
        width = 20, 
        height = 5,
    )
    Title.pack(side = "top", anchor="e", padx=10)

    srcURLName = Label(tab, 
        text="Source URL:",
        width = 20, 
        height = 1,
        fg = "white",
        bg = f"#333333",
    )
    srcURLName.pack(side = "top", anchor="e", padx=10)

    global srcURL
    srcURL = Label(tab, 
        text="url",
        width = 20, 
        height = 5,
    )
    srcURL.pack(side = "top", anchor="e", padx=10)

    AddyName = Label(tab, 
        text="Address:",
        width = 20, 
        height = 1,
        fg = "white",
        bg = f"#333333",
        wraplength=200
    )
    AddyName.pack(side = "top", anchor="e", padx=10)

    global Addy
    Addy = Label(tab, 
        text="address",
        width = 20, 
        height = 5,
    )
    Addy.pack(side = "top", anchor="e", padx=10)

    DescName = Label(tab, 
        text="Description:",
        width = 20, 
        height = 1,
        fg = "white",
        bg = f"#333333",
    )
    DescName.pack(side = "top", anchor="e", padx=10)

    global Desc
    Desc = Label(tab, 
        text="desc",
        width = 20, 
        height = 5,
    )
    Desc.pack(side = "top", anchor="e", padx=10)

    TimeName = Label(tab, 
        text="Time",
        width = 20, 
        height = 1,
        fg = "white",
        bg = f"#333333",
    )
    TimeName.pack(side = "top", anchor="e", padx=10)

    global Time
    Time = Label(tab, 
        text="url",
        width = 20, 
        height = 5,
    )
    Time.pack(side = "top", anchor="e", padx=10)
    
def update_info(title, url, desc, address, time):
    Title.configure(text=title)
    srcURL.configure(text=url)
    Desc.configure(text=desc)
    Addy.configure(text=address)
    Time.configure(text=time)