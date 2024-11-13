"""
-- notebook.py --
Class Notebook to controll and stroe notes
"""
import tkinter
from tkinter import Frame, END

# Local imports 
import gopy.api
from defaults import *  # pylint: disable=W0401
from text_scroll import TextBlock


class NoteBook:
    """
    A Notebook stores all notes by books
    """

    def __init__(self, parent_frame: tkinter.Frame) -> None:
        """
        """
        self.open:      bool            = False
        self.book_path: str             = None

        self.frame:     tkinter.Frame   = Frame(
            parent_frame,
            highlightthickness=0,
            bd=0,
            width=1,
            highlightbackground=BUTTON_COLOR
        )
        self.text:      TextBlock       = TextBlock(self.frame)
        self.api:       gopy.api        = gopy.api
        self.db_path: str = "./sql/poki_books.db"

    def set_book_path(self, path: str) -> None:
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
        Gets all note text from database
        """
        notes = self.api.GetNotesByPath(self.db_path, self.book_path)
        # if err != None:
        #     print(err)
        #     exit(0)
        return notes
        

    def get_current_text(self, start_index: str = '1.0',
                         end_index: str = END) -> str:
        """
        Get text displayed
        """
        return self.text.get(start_index, end_index)


    def clear_all(self) -> None:
        """
        Resets all notes
        """
        self.api.ResetNotes(self.db_path)
     
    def cache(self) -> None:
        """
        Add current books note to database
        """
        notes = self.get_current_text()
        err = self.api.AddNotesByPath(self.db_path, notes, self.book_path)
        if err != None:
            print(err)
            exit(1)
        return 
