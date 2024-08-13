"""
-- text_scroll_combo.py --

"""
import tkinter as tk
from tkinter import ttk, END
import json
from defaults import FONT, HEADING_SIZE

class TextScrollCombo(tk.Frame):
    """
    Combines frame for text and a scrollbar
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book_path = 'books/'
        self.cache_path = 'cache.json'

    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tk.Text(self)
        self.txt.config(
            font=(FONT, HEADING_SIZE),
            highlightthickness=0,
            borderwidth=0,
            padx=10,
            pady=10,
            wrap='word',
            relief='sunken'
            )

    # create a Scrollbar and associate it with txt
        self.scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set


    def insert(self, text, pos='1.0'):
        self.txt.config(state='normal')

        """
        insert text into textscrollcombo
        """
        self.txt.insert(pos, text)
        self.update()

    def append(self, text, add_space=False, add_newline=False):

        if add_space:
            self.insert(' '+text, END)
        elif add_newline:
            self.insert('\n'+text, END)
        else:
            self.insert(text, END)
        self.update()

    def clear(self):
        """
        Clears all text
        """
        self.txt.delete('1.0', END)
        self.update()

    def set_scrollbar(self, book_path):
        """
        Sets the scrollbar to the position last used stored in cache
        """
        with open(self.cache_path, 'r') as file:
            books_info = json.load(file)['books']
            if book_path in books_info:
                scrollbar_position = books_info[book_path]['scrollbar']
                self.scrollb.set(*books_info[book_path]['scrollbar'])
                self.txt.yview_moveto(scrollbar_position[0])
    
    def update(self):
        self.txt.grid(row=0, column=0, sticky='nsew')
        self.txt.config(state='disabled')

    def reset_text(self):
        self.txt = tk.Text(self)
        self.txt.config(
            font=(FONT, HEADING_SIZE),
            highlightthickness=0,
            borderwidth=0,
            padx=10,
            pady=10,
            wrap='word',
            relief='sunken'
            )
