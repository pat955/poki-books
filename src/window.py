"""
-- window.py --
bookbot window setup
TODO:
# Pictures
# Better loading
# Clean up code
# Chapters?
# Search
# Bookmark
# Highlight
# Keybinds
# Back to top button
# Add error handling
# user added themes
# fix theme bugs with view all and read
"""
import tkinter as tk
import os
import json
import platform
from functools import partial
from tkinter import Frame, Button, Tk, Checkbutton, Entry, Menu, Label
from library import Library

import gopy.api
from notes import NoteBook
from text_scroll import TextScrollCombo
from themes import AllThemes
from defaults import *  # pylint: disable=W0401
from basics import basic_button, basic_label, basic_entry, make_full_frame, make_basic_menu, info, contact


class BookBot:
    """
    Makes the bookbot window, all buttons, frames, checkboxes and so forth.
    """

    def __init__(self) -> None:
        self.__root = Tk()
        self.__root.title("PokiBooks")
        icon_data = 'static/icon.png'

        try:
            icon = tk.PhotoImage(file=icon_data)
            self.__root.iconphoto(True, icon)

        except Exception as e:
            print(e)
        self.__root.configure(background=COLOR)
        self.__root.protocol("WM_DELETE_WINDOW", self._quit)

        if platform.system() == 'Windows':
            self.__root.state('zoomed')  # This works on Windows
        else:
            # This works on some Unix systems
            self.__root.attributes("-zoomed", True)
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)

        self.current_book = None
        self.book_folder = 'books/'
        self.api = gopy.api
        
        
        if not os.path.exists(self.book_folder):
            os.makedirs(self.book_folder)

    # Frames and textscrollcombos
        self.text_container = make_full_frame(self.__root)

        self.text_frame = TextScrollCombo(self.text_container, bg=COLOR)
        self.text_frame.grid(column=0, row=0, sticky="nsew")

        self.all_books_menu = TextScrollCombo(self.text_container, bg=COLOR)

        # Change to textscrollcombo?
        self.sidebar = Frame(
            self.text_container,
            bg=COLOR,
            highlightthickness=1)
        self.sidebar.grid(column=1, row=0, sticky="ens")

    # Menus
        # Main Menus
        self.menubar = make_basic_menu(menubar=self.__root, bg=COLOR)
        self.settings_menu = make_basic_menu(
            menubar=self.menubar, bg=BUTTON_COLOR)
        self.books_menu = make_basic_menu(
            menubar=self.menubar, bg=BUTTON_COLOR)
        self.help_menu = make_basic_menu(menubar=self.menubar, bg=BUTTON_COLOR)

        # Settings
        self.settings_menu.add_command(
            label="Fullscreen",
            command=self.toggle_fullscreen)

        self.settings_menu.add_separator()

        self.settings_menu.add_command(
            label="Refresh books",
            command=self.refresh_books)

        self.settings_menu.add_command(
            label='Set default theme',
            command=self.not_implemented)

        self.settings_menu.add_command(
            label="Toggle Sidebar",
            command=self.toggle_sidebar)

        self.settings_menu.add_separator()
        self.settings_menu.add_command(label="Exit", command=self._quit)

        # Notes
        self.notebook = NoteBook(self.sidebar)
        self.notes_button = Button(
            self.sidebar,
            text='Notebook',
            bg=BUTTON_COLOR,
            command=self.notebook.toggle,
            highlightthickness=0,
            font=(FONT, FONT_SIZE)
        )

        # Library
        self.library = Library(self, self.book_folder)

        # Book menu
        self.books_menu.add_command(
            label="Go to all books",
            command=self.library.view_all)

        self.books_menu.add_separator()

        self.books_menu.add_command(
            label="Clear Notes",
            command=self.reset_all_notes)

        self.books_menu.add_separator()

        self.books_menu.add_command(
            label="Add book",
            command=self.library.add_filedialog)

        self.books_menu.add_command(
            label="Remove book",
            command=self.library.remove_page)

        # Help Menu
        self.help_menu.add_command(
            label="Contact", command=partial(
                contact, self))
        self.help_menu.add_command(label="About", command=partial(info, self))

        # Menubar
        self.menubar.add_cascade(label="Settings", menu=self.settings_menu)
        self.menubar.add_cascade(label="Books", menu=self.books_menu)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        self.__root.config(menu=self.menubar)

    # Buttons
        self.all_books_button = basic_button(
            self.sidebar, 'All Books', self.library.view_all)
        self.add_n_read_button = basic_button(
            self.sidebar, 'Add n\' Read Book', self.library.add_and_open)
        self.refresh_button = basic_button(
            self.sidebar, 'Refresh', self.check_entries)

        self.all_books_button.pack(side='top', fill='x')
        self.add_n_read_button.pack(side='top', fill='x', pady=10)
        self.refresh_button.pack(side='top', fill='x')

    # Entries and Labels
        self.text_size_label = basic_label(self.sidebar, 'Text Size')
        self.text_size_entry = basic_entry(self.sidebar)

        self.text_size_label.pack(side='top', fill='x', pady=5)
        self.text_size_entry.pack(side="top", fill="x")

        self.padding_label = basic_label(self.sidebar, 'Padding')
        self.padding_entry = basic_entry(self.sidebar)

        self.padding_label.pack(side='top', fill='x', pady=5)
        self.padding_entry.pack(side="top", fill="x")

    # Checkboxes
        self.centered = tk.BooleanVar()
        self.center_checkbutton = Checkbutton(
            self.sidebar, bg=COLOR,
            highlightthickness=0,
            command=self.center,
            text='Center text',
            font=(FONT, FONT_SIZE),
            fg=FONT_COLOR,
            variable=self.centered
        )
        self.center_checkbutton.pack(side='top', fill='x', pady=10)

    # Notes
        self.notes_button.pack(side='top', fill='x')

    # Library
        self.library = Library(self, self.book_folder)

    # Themes
        self.themes_button = Menu(
            self.__root,
            tearoff=0,
            bg=BUTTON_COLOR,
            font=(
                FONT,
                FONT_SIZE))
        i = 0
        themes = AllThemes().get_all_themes()
        for theme in themes:
            theme.add(self, i)
            i += 1
        self.menubar.add_cascade(label="Themes", menu=self.themes_button)
        self.__root.mainloop()


    def reset_all_notes(self) -> None:
        """
        Clears all notes from database
        """
        self.notebook.clear_all()

    def cache_book(self) -> None:
        """
        Caches current book
        """
        self.notebook.book_path = self.current_book
        self.notebook.cache()
        scrollbar_pos = self.text_frame.scrollb.get()
        print(scrollbar_pos)


    def clear_text(self) -> None:
        """
        Clear all text from text_frame. For debugging
        """
        
        self.text_frame.clear_text()

    # change theme
    def change_theme(
            self,
            color: str = COLOR,
            font_color: str = FONT_COLOR,
            button_color: str = BUTTON_COLOR,
            active_background: str = ACTIVE_BACKGROUND,
            active_font: str = ACTIVE_FONT,
            font: str = FONT,
            font_size: int = FONT_SIZE,
            heading_size: int = HEADING_SIZE
    ) -> None:
        """
        Sets theme
        TODO: improve function, fonts
        """
        COLOR = color
        FONT_COLOR = font_color
        BUTTON_COLOR = button_color
        ACTIVE_BACKGROUND = active_background
        ACTIVE_FONT = active_font
        FONT = font
        FONT_SIZE = font_size
        HEADING_SIZE = heading_size

        frames = [
            self.__root,
            self.sidebar,
            self.notebook.frame,
            self.text_frame,
            self.menubar,
            self.all_books_menu,
            self.all_books_menu.txt,
            *(self.text_container.winfo_children())
        ]

        for frame in frames:
            try:
                if frame in [self.sidebar, self.text_frame]:
                    frame.config(bg=COLOR)

                else:
                    frame.config(
                        activebackground=ACTIVE_BACKGROUND,
                        activeforeground=ACTIVE_FONT
                    )
            except tk.TclError:
                pass

            for widget in frame.winfo_children():
                try:
                    widget.config(bg=COLOR)
                except tk.TclError:
                    pass

                try:
                    widget.config(fg=FONT_COLOR)
                except tk.TclError:
                    pass

                if isinstance(widget, Checkbutton):
                    widget.config(
                        activebackground=COLOR,
                        activeforeground=ACTIVE_FONT
                    )

                elif isinstance(widget, Button):
                    widget.config(
                        bg=BUTTON_COLOR,
                        activebackground=ACTIVE_BACKGROUND,
                        activeforeground=ACTIVE_FONT
                    )

                elif isinstance(widget, Entry):
                    widget.config(bg=BUTTON_COLOR)

                elif isinstance(widget, Label):
                    widget.config(bg=BUTTON_COLOR)

                widget.update()

    def check_entries(self) -> None:
        """
        Check entries in option sidebar, like text size or padding
        """
        entries = {
            self.text_size_entry: self.change_text_size,
            self.padding_entry: self.change_padx,
        }
        for entry, func in entries.items():
            if entry.get():
                func()

    def change_padx(self) -> None:
        """
        Change padding in x direction in text_frame TextScrollCombo
        """
        self.text_frame.txt.config(padx=self.padding_entry.get())

    def change_text_size(self) -> None:
        """
        Changes text size to number from entry TODO: add edgecases/errorhandling
        """
        self.text_frame.txt.configure(font=(FONT, self.text_size_entry.get()))

    def center(self) -> None:
        """
        Centers text in main text frame in book_frame textscrollcombo
        """
        self.text_frame.center_text()

    def refresh_books(self) -> None:
        """
        Adds and updates books in book folder to database.
        """
        self.library.recheck_books()

    def toggle_sidebar(self) -> None:
        """
        Toggles sidebar
        """
        if self.sidebar.winfo_viewable():
            self.sidebar.grid_remove()
        else:
            self.sidebar.grid(column=1, row=0, sticky="ens")

    def toggle_fullscreen(self) -> None:
        """
        Toggles fullscreen
        TODO: Check compat with windows
        """
        self.__root.attributes("-fullscreen",
                               not self.__root.attributes('-fullscreen'))
        self.__root.bind(
            "<Escape>",
            lambda x: self.__root.attributes(
                "-fullscreen",
                False))

    def _quit(self) -> None:
        """
        Quit program
        """
        try:
            self.cache_book()
        except Exception:
            print("Didnt cache book when quitting, ignore if no books were opened")
            pass
        self.__root.quit()
        self.__root.destroy()

    def not_implemented(self) -> None:
        """
        not implemented error
        """
        self.text_frame.show_error("Error: Not Implemented", "")
