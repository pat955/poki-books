"""
-- notebook.py --
Class Notebook to controll and stroe notes
"""
import json
import tkinter
from tkinter import Frame, Text, END
from defaults import *  # pylint: disable=W0401
from text_scroll import TextBlock

class NoteBook:
    """
    A Notebook stores all notes by books
    """

    def __init__(self, parent_frame: tkinter.Frame, cache_path: str) -> None:
        """
        """
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
        self.text = TextBlock(self.frame)

    def set_path(self, path: str) -> None:
        """
        sets current book path
        """
        self.book_path = path

    def toggle(self) -> None:
        """
        Toggle on and of notes. Inserts notes from cache
        """
        if self.open:
            self.text.clear()
            self.frame.pack_forget()
        else:
            self.frame.pack(side='bottom', fill='both', expand=True, pady=15)
            self.text.config(state='normal')
            self.text.write(self.get())
            
            self.text.config(state='normal')
            self.text.pack(anchor='n', fill='both', expand=True)

        self.open = not self.open

    def update(self) -> None:
        """
        Updates text
        """
        if self.open:
            self.text.update()

    def get(self) -> str:
        """
        Gets all note text from cache
        """
        with open(self.cache_path, 'r') as file:
            file_data = json.load(file)
            if self.book_path is None:
                return file_data['books']['notes']
            return file_data['books'][self.book_path]['notes']

    def get_current_text(self, start_index: str ='1.0', end_index:str =END) -> str:
        """
        Get text displayed
        """
        return self.text.get(start_index, end_index)
