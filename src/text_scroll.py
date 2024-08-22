"""
-- text_scroll.py --

"""
import tkinter as tk
from tkinter import ttk, END
import json
from defaults import FONT, HEADING_SIZE
from basics import make_full_frame

class TextScrollCombo(tk.Frame):
    """
    Combines frame for text and a scrollbar
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book_path = 'books/'
        self.cache_path = 'cache.json'
        self.multi_block = False
        self.text_blocks = []

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
        if self.multi_block:
            self.text_blocks = []
            return
        self.txt.config(state='normal')
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
                if self.multi_block:
                    for block in self.text_blocks:
                        block.yview_moveto(scrollbar_position[0])
                    return    
                self.txt.yview_moveto(scrollbar_position[0])
    
    def update(self):
        if self.multi_block:
            for block in self.text_blocks:
                block.grid(row=0, column=0, sticky='nsew')
                block.config(state='disabled')
            return
        self.txt.grid(row=0, column=0, sticky='nsew')
        self.txt.config(state='disabled')


    def reset_text(self):
        self.txt = self.new_text(self)
    
    def new_text(self, root):
        txt = tk.Text(root)
        txt.config(
            font=(FONT, HEADING_SIZE),
            highlightthickness=0,
            borderwidth=0,
            padx=10,
            pady=10,
            wrap='word',
            relief='sunken'
            )
        return txt

    def toggle_multiblock(self, keep=False):
        if self.multi_block:
            print(NotImplementedError)
            return
        if keep:
            print(NotImplementedError)
            return
        self.multi_block = True
        self.txt = make_full_frame(self)

    def insert_block(self, text):
        # compare if same TODO
        if not self.multi_block:
            print('MULTIBLOCK NOT ENABLED')
            return
        
        new_block = self.new_text(self.txt)
        i = len(self.text_blocks)
        new_block.insert('1.0', text)

        new_block.grid(row=i, column=0, sticky='nsew')
        new_block.config(state='disabled')
        self.text_blocks.append(new_block)


