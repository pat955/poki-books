"""
-- library.py --
Class Library, collection of books
TODO:
add remove function
"""

import shutil
import os
from functools import partial
from pathlib import Path
from tkinter import filedialog, Button, Label
from defaults import *  # pylint: disable=W0401
from basics import dir_empty, prettify_title
from book_types import load_book
import gopy
import gopy.api


class Library:
    """
    Collection of all books
    """

    def __init__(self, book_bot, folder_path: str = 'books/') -> None:
        """
        """
        self.book_bot = book_bot
        self.__root = self.book_bot.text_frame
        self.notebook = self.book_bot.notebook
        self.folder_path = folder_path
        self.db_path = "./sql/poki_books.db"

    def remove(self) -> None:
        """
        Not implemented. Removes book from library
        """
        self.book_bot.text_frame.show_error(
            'NotImplementedError',
            'remove function current not implemented, simply remove book from folder')

    def add(self) -> str:
        """
        Add book from filedialog.
        Returns book path
        """
        api = gopy.api

        path = filedialog.askopenfilename(
            initialdir=str(Path.home() / "Downloads"))

        if path:
            try:
                shutil.move(path, self.folder_path)
                a = api.AddBook(self.db_path,
                    book=api.Book(
                        Title="path",
                        Content="something here",
                        handle=200))
                print(a)
            except Exception as e:
                print(e)
            return path
        return ''

    def see_all(self) -> None:
        """
        TODO: Rename to library_view
        TODO: fix visual bugs
        Shows all books in books folder, presents them as buttons.
        """
        self.__root.clear_text()

        i, j = 0, 0

        if dir_empty(self.folder_path):
            label = Label(
                self.__root.txt,
                text='No Books Added Yet',
                font=(FONT, HEADING_SIZE),
                bg=COLOR,
                fg=FONT_COLOR,
                activebackground=ACTIVE_BACKGROUND,
                activeforeground=ACTIVE_FONT,
                width=0,
                justify='center'
            )
            label.grid(sticky='nesw', pady=20, padx=20)
            return

        for file in os.scandir(self.folder_path):
            if i % 5 == 0:
                j += 1
                i = 0
            txt = prettify_title(file.name)
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
                width=19
            )
            button.grid(row=j, column=i, sticky='n', pady=10, padx=20)
            i += 1

    def add_and_open(self) -> None:
        """
        Add book through filedialog, and opens it to instantly read
        """
        path = self.add()
        if path:
            self.read(self.folder_path + path.split('/')[-1])

    def read(self, path) -> None:
        """
        Sets this book as current, changes book in notebook
        Checks entries, inserts notes and loads book contents
        """
        # self.cache_book()
        self.book_bot.current_book = path
        self.notebook.set_path(self.book_bot.current_book)

        self.book_bot.check_entries()
        self.notebook.update()
        load_book(self.__root, path)
