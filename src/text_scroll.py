"""
-- text_scroll.py --

"""
import random
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

        # Multi block system
        self.blocks_enabled = False
        self.text_blocks = []
        self.block_system_frame = None
        self.block_frame = None
        self.block_scrollb = ttk.Scrollbar(self.block_system_frame)

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
                self.block_scrollb.set(*books_info[book_path]['scrollbar'])  
                self.txt.yview_moveto(scrollbar_position[0])
    
    def clear(self):
        if self.blocks_enabled:
            for block in self.text_blocks:
                block.clear()
        self.txt.clear()

    def reset_text(self):
        self.txt = TextBlock(self).New()
        self.txt.update()
        self.scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set
    
    def toggle_scrollbars(self):
        if self.blocks_enabled:
            self.scrollb.forget()
            self.block_scrollb.grid(row=0, column=1, sticky='nsew')
        else:
            self.block_scrollb.forget()
            self.scrollb.grid(row=0, column=1, sticky='nsew')
        

    def toggle_txt(self):
        if self.txt.winfo_visual():            
            self.txt.forget()
            return
        self.reset_text()

    def toggle_multiblock(self):
        self.toggle_txt()
        if self.blocks_enabled:
            self.toggle_scrollbars()
            self.text_blocks = []
            self.block_system_frame.destory()
        else:
            self.block_system_frame = make_full_frame(self)
            self.block_system_frame.grid_columnconfigure(0, weight=1)
            self.block_frame = make_full_frame(self.block_system_frame)
    
        self.toggle_scrollbars()

        self.blocks_enabled = not self.blocks_enabled

    def insert_block(self, text):
        # compare if same TODO
        if not self.blocks_enabled:
            print('MULTIBLOCK NOT ENABLED')
            return
        if not text:
            return

        new_block = TextBlock(self.block_frame).New()
        i = len(self.text_blocks)
        self.block_frame.grid_rowconfigure(i, weight=1)
        new_block.write(text)

        new_block.update(pos_row=i)
        self.text_blocks.append(new_block)


class TextBlock(tk.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def New(self):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        self.config(
            font=(FONT, HEADING_SIZE),
            highlightthickness=0,
            borderwidth=0,
            padx=10,
            pady=10,
            wrap='word',
            relief='sunken',
            bg= random.choice(colors)
            )
        return self
    
    def write(self, text, pos='1.0'):
        self.config(state='normal')

        """
        write text into textscrollcombo
        """
        self.insert(chars=text, index=pos)
        self.update()

    def append(self, text, add_space=False, add_newline=False):
        if add_space:
            self.write(' '+text, END)
        elif add_newline:
            self.write('\n'+text, END)
        elif add_space and add_newline:
            self.write('\n '+text, END)
        else:
            self.write(text, END)
        self.update()

    def update(self, pos_row=0, pos_column=0, sticky_dir='nsew'):
        self.grid(row=pos_row, column=pos_column, sticky=sticky_dir)
        self.config(state='disabled')

    def clear(self):
        self.config(state='normal')
        self.delete('1.0', END)
        self.update()



        # def toggle_center(self):
    #     self.centered = not self.centered
    #     if self.blocks_enabled:
    #         self.toggle_center_blocks()
    #         return
        
    #     if not self.centered:
    #         self.txt.tag_configure("center", justify='center')
    #         self.txt.tag_add("center", "1.0", "end")
    #         return
    #     self.txt.tag_delete("center")

    # def toggle_center_blocks(self):
    #     if not self.centered:
    #         self.block_wrapper(TextBlock.tag_configure, "center", justify="center")
    #         self.block_wrapper(TextBlock.tag_add, "center", "1.0", "end")
    #     else:
    #         self.block_wrapper(TextBlock.tag_delete, "center")

    # def block_wrapper(self, func, *args, **kwargs):
    #     # if not self.blocks_enabled:
    #     #     print('ERRROORORORORO')
    #     #     return
    #     for block in self.text_blocks:
    #         func(block, args, kwargs)
    #         print(block.tag_names(index=None))