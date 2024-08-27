"""
-- text_scroll.py --

"""
import tkinter as tk
from tkinter import ttk, END
import json
from defaults import *  # pylint: disable=W0401


class TextScrollCombo(tk.Frame):
    """
    Combines frame for text and a scrollbar
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.book_path = 'books/'
        self.cache_path = 'cache.json'
        # Customization
        # self.centered = False

    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = TextBlock(self).new()
        self.txt.update()

        self.scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set

    def set_scrollbar(self, book_path: str) -> None:
        """
        Sets the scrollbar to the position last used stored in cache
        """
        with open(self.cache_path, 'r') as file:
            books_info = json.load(file)['books']
            if book_path in books_info:
                scrollbar_position = books_info[book_path]['scrollbar']
                self.scrollb.set(*books_info[book_path]['scrollbar'])
                self.txt.yview_moveto(scrollbar_position[0])

    def reset(self) -> None:
        """
        Reset text and scrollbar
        """
        self.txt = TextBlock(self).new()
        self.txt.update()
        self.scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set

    def clear_text(self) -> None:
        """
        Clears all text
        """
        self.txt.clear()

    def insert_text(self, text: str, tag: str = None,
                    pos: str = '1.0') -> None:
        """
        insert text with a tag and position
        """
        self.txt.write(text, tag, pos)

    def append_text(
            self,
            text: str,
            tag: str = None,
            add_space: bool = False,
            add_newline: bool = False
    ) -> None:
        """
        Append text with tag, add space, newline or both
        """
        self.txt.append(text, tag, add_space, add_newline)

    def center_text(self) -> None:
        """
        toggles centering of text
        """
        self.txt.toggle_center()

    def update_text(self, pos_row=0, pos_column=0, sticky_dir='nsew'):
        """
        updates text
        TODO: do i need pos_row and pos_column?
        """
        self.txt.update(pos_row, pos_column, sticky_dir)


class TextBlock(tk.Text):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tag_configure("bold", font=(FONT, FONT_SIZE, "bold"))
        self.tag_configure("h1", font=(FONT, H1), justify='center')
        self.tag_configure("italic", font=(FONT, FONT_SIZE, "italic"))
        self.tag_configure("center", justify='center')
        self.centered = False

    def new(self):
        """
        Makes a new TextBlock
        """
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

    def write(self, text: str, tag: str = None, pos: str = '1.0') -> None:
        """
        TODO: add this
        """
        self.config(state='normal')
        if tag:
            i = self.index(tk.INSERT)
            self.insert(tk.INSERT, text)

            j = self.index(tk.INSERT)
            self.tag_add(tag, i, j)
        else:
            self.insert(chars=text, index=pos)
        self.update()

    def append(self, text: str, tag: str = None,
               add_space: bool = False, add_newline: bool = False) -> None:
        """
        TODO: reformat append function
        """
        if add_space:
            self.write(' ' + text, tag, END)
        elif add_newline:
            self.write('\n' + text, tag, END)
        elif add_space and add_newline:
            self.write('\n ' + text, tag, END)
        else:
            self.write(text, tag, END)
        self.update()

    def update(self, pos_row: int = 0, pos_column: int = 0, sticky_dir: str = 'nsew') -> None:
        """
        Refreshed text
        """
        self.grid(row=pos_row, column=pos_column, sticky=sticky_dir)
        self.config(state='disabled')


    def clear(self) -> None:
        """
        Clears all text
        """
        self.config(state='normal')
        self.delete('1.0', END)
        self.update()

    def toggle_center(self) -> None:
        """
        Toggle centered text
        """
        if not self.centered:
            self.tag_add("center", "1.0", END)
        else:
            self.tag_remove('center', "1.0", END)
        self.centered = not self.centered
