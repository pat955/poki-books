"""
-- library.py --
TODO:
add remove function
add docs

"""

import shutil
import os
from functools import partial
from pathlib import Path
from tkinter import filedialog, Button, Label
from defaults import * 
from basics import dir_empty
from book_types import load_book

class Library:
    def __init__(self, window, folder_path='books/'):
        self.__window = window
        self.__root = self.__window.text_frame
        self.notebook = self.__window.notebook
        self.folder_path = folder_path

    def remove(self): # Returns: None
        """
        Not implemented
        """
        self.__window.not_implemented()


    def add(self): # Returns: str 
        """
        Add book from filedialog. Returns book path
        """
        path = filedialog.askopenfilename(initialdir = str(Path.home() / "Downloads"))
        if path:
            try:
                shutil.move(path, self.folder_path)
            except Exception as e:
                print(e)
            return path

    def see_all(self): # Returns: None
        """
        Shows all books in books folder, presents them as buttons. 
        """
        self.__root.clear()
        
        i, j = 0, 0
        
        if dir_empty(self.folder_path):
            label = Label(
                self.__root.txt,
                text=f'No Books Added Yet',
                font=(FONT, HEADING_SIZE),
                bg=COLOR,
                fg=FONT_COLOR,
                activebackground=ACTIVE_BACKGROUND,
                activeforeground=ACTIVE_FONT,
                width=0
                )
            label.grid(sticky='nesw', pady=10, padx=20)
            return
        
        for file in os.scandir(self.folder_path):
            if  i % 6 == 0:
                j += 1
                i = 0
            txt = file.name.split('.')[0].replace('_', ' ').capitalize()
            path = self.folder_path + file.name
            button = Button(
                self.__root.txt,
                text=f'{txt}',
                bg=BUTTON_COLOR,
                font=(FONT, HEADING_SIZE),
                fg=FONT_COLOR,
                activebackground=ACTIVE_BACKGROUND,
                activeforeground=ACTIVE_FONT,
                command=partial(self.read, path),
                width=16
                )
            button.grid(row=j, column=i, sticky='n', pady=10, padx=20)
            i += 1

    def add_and_open(self): # Returns: None
        """
        Add book through filedialog, and opens it to instantly read
        """
        path = self.add()
        if path:
            self.read(self.folder_path + path.split('/')[-1])

    def read(self, path): # Returns: None
        # self.cache_book()
        self.__window.current_book = path
        self.notebook.change_book(self.__window.current_book)

        self.__window.check_entries()
        self.notebook.update()
        load_book(self.__root, path)