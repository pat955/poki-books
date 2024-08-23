"""
-- text_scroll.py --

"""
import tkinter as tk
from tkinter import ttk, END
import json
from defaults import *

class TextScrollCombo(tk.Frame):
    """
    Combines frame for text and a scrollbar
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book_path = 'books/'
        self.cache_path = 'cache.json'
        # Customization
        # self.centered = False

    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = TextBlock(self).New()
        self.txt.update()

        self.scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set

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
    
    def clear(self):
        self.txt.clear()

    def reset(self):
        self.txt = TextBlock(self).New()
        self.txt.update()
        self.scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set


class TextBlock(tk.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tag_configure("bold", font=(FONT, FONT_SIZE, "bold"))
        self.tag_configure("h1", font=(FONT, HEADING_SIZE))
        self.tag_configure("italic", font=(FONT, FONT_SIZE, "italic"))
        self.tag_configure("center", justify='center')
        self.centered = False


    def New(self):
        self.config(
            font=(FONT, HEADING_SIZE),
            highlightthickness=0,
            borderwidth=0,
            padx=10,
            pady=10,
            wrap='word',
            relief='sunken'
            )
        return self
    
    def write(self, text, tag=None, pos='1.0'):
        self.config(state='normal')
        if tag:
            i = self.index(tk.INSERT)
            self.insert(tk.INSERT, text)

            j = self.index(tk.INSERT)
            self.tag_add(tag, i, j)
        else:    
            self.insert(chars=text, index=pos)
        self.update()

    def append(self, text, tag=None, add_space=False, add_newline=False):
        if add_space:
            self.write(' '+text, tag, END)
        elif add_newline:
            self.write('\n'+text, tag, END)
        elif add_space and add_newline:
            self.write('\n '+text, tag, END)
        else:
            self.write(text, tag, END)
        self.update()

    def update(self, pos_row=0, pos_column=0, sticky_dir='nsew'):
        self.grid(row=pos_row, column=pos_column, sticky=sticky_dir)
        self.config(state='disabled')

    def clear(self):
        self.config(state='normal')
        self.delete('1.0', END)
        self.update()

    def toggle_center(self):
        if not self.centered:
            self.tag_add("center", "1.0", END)
        else:
            self.tag_remove('center', "1.0", END)
        self.centered = not self.centered
