"""
-- library.py --
Class Library, collection of books
TODO:
add remove function
"""

import shutil
import os
import gopy.api
from functools import partial
from pathlib import Path
from tkinter import filedialog, Button, Label
from defaults import *  # pylint: disable=W0401
from basics import dir_empty, prettify_title
from book_types import prepare_book
from text_scroll import TextScrollCombo
from notes import NoteBook


class Library:
    """
    Collection of all books
    """

    def __init__(self, book_bot, folder_path: str = 'books/') -> None:
        """
        """
        self.book_bot = book_bot # BookBot type
        self.__root:        TextScrollCombo = self.book_bot.text_frame
        self.notebook:      NoteBook = self.book_bot.notebook
        self.folder_path:   str = folder_path
        self.db_path:       str = "./sql/poki_books.db"

    def remove(self, path) -> None:
        """
        Removes book from database
        TODO: remove from folder
        """
        api = gopy.api
        print(f"Trying to remove book at: {path}")

        err = api.RemoveBook(path)
        print(f"Removing book... Error: {err}")
        ## debug
        shutil.move(path, "~/Downloads")
    

    def add(self) -> str :
        """
        Add book from filedialog.
        Returns book path
        """
        api = gopy.api

        path = filedialog.askopenfilename(
            initialdir=str(Path.home() / "Downloads"))

        if path:
            book, err = prepare_book(api.Book(
                Path=path,
                handle=200
            ))
            if err != None:
                print(f"ERROR {err}")
                return ""
            
            try:
                new_path = shutil.move(path, self.folder_path)
                book.Path = new_path
            except Exception as e:
                print(e)
                return ""
            try:
                api.AddBook(self.db_path, book)
            except Exception as e:
                print(f"NEW ERROR {e}")
                return ""            
            return path
        return ''
    
    def add_and_open(self) -> None:
        """
        Add book through filedialog, and opens it to instantly read
        """
        path = self.add()
        if path:
            self.read(self.folder_path + path.split('/')[-1])

    
    def read(self, path: str) -> None:
        """
        Sets this book as current, changes book in notebook
        Checks entries, inserts notes and loads book contents
        """
        self.__root.clear_text()
        book = gopy.api.GetBookByPath(self.db_path, path)
        
        # self.cache_book()
        self.book_bot.current_book = path
        self.notebook.set_path(self.book_bot.current_book)

        self.book_bot.check_entries()
        self.notebook.update()
        self.__root.insert_text(book.Content)

    def view_all(self) -> None:
        """
        TODO: fix visual bugs
        Shows all books in books folder, presents them as buttons.
        """
        self.__root.clear_text()

        i, j = 0, 0
        books = gopy.api.GetAllBooks(self.db_path)

        if books == []:
            self.__root.show_error("EmptyFolderError", "No Books Added Yet! (Potential database error)")
            return
        
        for book in books:
            if i % 5 == 0:
                j += 1
                i = 0
            if book.Title:
                title = book.Title
            else:
                title = prettify_title(book.Path.strip("books/"))               

            self.view_all_button(title, book.Path).grid(row=j, column=i, sticky='n', pady=10, padx=15)
            i += 1

    def recheck_books(self) -> None:
        if dir_empty(self.folder_path):
            self.__root.show_error("Nothing to refresh")


    def view_all_button(self, name: str, path: str) -> Button:
        return Button(
                self.__root.txt,
                text=f'{name}',
                bg=BUTTON_COLOR,
                font=(FONT, HEADING_SIZE),
                fg=FONT_COLOR,
                activebackground=ACTIVE_BACKGROUND,
                activeforeground=ACTIVE_FONT,
                command=partial(self.read, path),
                width=25
            )