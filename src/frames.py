""" 
-- frames.py --

"""
from tkinter import Frame

def make_full_frame(root): # Returns: tkinter.Frame
    """
    Returns a frame with "fullscreen" config 
    """
    f = Frame(root)
    f.columnconfigure(0, weight=1)
    f.rowconfigure(0, weight=1)
    f.grid(column=0, row=0, sticky="nsew")
    return f
