import tkinter as tk
import math
from functools import partial
from defaults import *

def make_resizable(options, text_container):
    options.bind("<Button-1>", on_resize_start)
    options.bind("<B1-Motion>", on_resize_motion)
    global apply_button
    apply_button = tk.Button(options, text='Apply Changes', bg=BUTTON_COLOR, command=partial(apply, options, text_container), highlightthickness=0, font=(FONT, FONT_SIZE))
    

def on_resize_start(event):
    options = event.widget
    options._resize_start_x = event.x
    options._resize_width = options.winfo_width()
    try:
        apply_button.pack_info()
    except:
        apply_button.pack(side='bottom', fill='x')


def on_resize_motion(event):
    options = event.widget
    text_container = event.widget
    
    width = max(options.winfo_width() - (event.x - options._resize_start_x), 50)
    x = options.winfo_x() + options.winfo_width() - width
    
    options_frame_width = options.winfo_width() 
    text_container_width = text_container.winfo_width() - (x + width)

    global weight_ratio

    # Calculate the ratio, ensure the ratio is positive
    weight_ratio = int((abs(options_frame_width)/abs(text_container_width))*200000), int((abs(text_container_width)/abs(options_frame_width))*200000)
    
    # LIVE UPDATES!!!
    options.place(x=x, width=width, height=options.winfo_height())


def apply(options, text_container):
    text_container.columnconfigure(0, weight=weight_ratio[1])
    text_container.columnconfigure(1, weight=weight_ratio[0])
    text_container.grid()
    options.grid(column=1, row=0, sticky="nsew")
    apply_button.pack_forget()

def make_basic_full_frame(root):
    f = tk.Frame(root)
    f.columnconfigure(0, weight=1)
    f.rowconfigure(0, weight=1)
    f.grid(column=0, row=0, sticky="nsew")
    return f