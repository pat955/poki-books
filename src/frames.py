"""
-- frames.py --

"""
import json
from tkinter import Frame, Text
from defaults import *

class NoteBook:
    """"
    """
    def __init__(self, parent_frame, cache_path):
        self.open = False
        self.cache_path = cache_path
        self.book_path = None

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

    def change_book(self, path):
        self.book_path = path


    def toggle(self): # Returns: None
        """
        Toggle on and of notes. Inserts notes from cache
        """
        if self.open:
            self.text.config(state='disabled')
            self.text.delete('1.0', 'end')
            self.frame.pack_forget()
            self.open = False
            return
        self.text.config(state='normal')
        self.frame.pack(side='bottom', fill='both', expand=True, pady=15)
        self.text.insert('insert', self.get())
        self.text.pack(fill='both', expand=True, anchor='n')
        self.open = True

    def update(self):
        if self.open:
            self.text.delete('1.0', 'end')
            self.text.insert('insert', self.get())

    def get(self):
        with open(self.cache_path, 'r') as file:
            file_data = json.load(file)
            if self.book_path is None:
                return file_data['books']['notes']
            return file_data['books'][self.book_path]['notes']

    def get_current(self):
        return self.text.get("1.0", 'end')


def make_full_frame(root): # Returns: tkinter.Frame
    """
    Returns a frame with "fullscreen" config 
    """
    f = Frame(root)
    f.columnconfigure(0, weight=1)
    f.rowconfigure(0, weight=1)
    f.grid(column=0, row=0, sticky="nsew")
    return f
