"""
-- frames.py --

"""
import json
from tkinter import Frame, Text
from defaults import *

class NoteBook():
    def __init__(self, parent_frame):
        self.open = False
        # text scrollcombo replacement? redo
        self.frame = Frame(
            parent_frame,
            highlightthickness=0,
            bd=0,
            width=1,
            highlightbackground=BUTTON_COLOR
            )
        self.text = Text(
            self.frame,
            state='normal',
            wrap='word',
            font=(FONT, FONT_SIZE),
            fg=FONT_COLOR,
            bg=COLOR,
            width=1
            )
        
    def toggle(self, cache_path, book_path): # Returns: None
        """
        Toggle on and of notes. Inserts notes from cache
        """
        if self.open:
            self.text.config(state='disabled')
            self.text.delete('1.0', 'end')
            self.frame.pack_forget()
            self.open = False
        else:
            self.text.config(state='normal')
            self.frame.pack(side='bottom', fill='both', expand=True, pady=15)
            self.text.insert('insert', self.get(cache_path, book_path))
            self.text.pack(fill='both', expand=True, anchor='n')
            self.open = True

    def update(self):
        if self.open:
            self.text.delete('1.0', 'end')
            self.text.insert('insert', self.get(cache_path, book_path))
    
    def get(self, cache_path, book_path ):
        with open(cache_path, 'r') as file:
            file_data = json.load(file)
            if book_path is None:
                return file_data['books']['notes']
            return file_data['books'][book_path]['notes']


def make_full_frame(root): # Returns: tkinter.Frame
    """
    Returns a frame with "fullscreen" config 
    """
    f = Frame(root)
    f.columnconfigure(0, weight=1)
    f.rowconfigure(0, weight=1)
    f.grid(column=0, row=0, sticky="nsew")
    return f
