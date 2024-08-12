"""
-- basics.py --

"""
import os
from tkinter import Button, Label, Entry, Frame
from defaults import BUTTON_COLOR, FONT, FONT_SIZE, ACTIVE_BACKGROUND, ACTIVE_FONT, COLOR

def basic_button(root, name, command):
    """
    DRY principle
    Basic button with the only variation being name and command
    """
    return Button(
        root,
        text=name,
        bg=BUTTON_COLOR,
        command=command,
        highlightthickness=0,
        font=(FONT, FONT_SIZE),
        activebackground=ACTIVE_BACKGROUND,
        activeforeground=ACTIVE_FONT
        )

def basic_label(root, name):
    return Label(root, text=name, bg=COLOR, font=(FONT, FONT_SIZE))

def basic_entry(root):
    return Entry(root, bg=BUTTON_COLOR, highlightthickness=0) 
   
def make_full_frame(root): # Returns: tkinter.Frame
    """
    Returns a frame with "fullscreen" config 
    """
    f = Frame(root)
    f.columnconfigure(0, weight=1)
    f.rowconfigure(0, weight=1)
    f.grid(column=0, row=0, sticky="nsew")
    return f

def dir_empty(dir_path): # Returns: bool
    return not any((True for _ in os.scandir(dir_path)))