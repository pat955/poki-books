""" 
-- window.py --
bookbot window, all setup
TODO:
# Pictures
# Better loading
# Clean up code
# Search
# Bookmark
# Highlight
# Keybinds
# Back to top button
# Add error handling
# Pdf support
# theme guide
# No books added screen
# fix spec files
# changelog
# Mac release
"""
import tkinter as tk
import os
import json
import shutil
from functools import partial
from tkinter import Frame, Button, Tk, Checkbutton, Entry, Menu, filedialog
from pathlib import Path
from frames import NoteBook, make_full_frame
from text_scroll import TextScrollCombo
from themes import AllThemes
from menu import make_main_menu, info
from defaults import *
from basics import basic_button, basic_label, basic_entry
import pkgutil
import platform


class BookBot:
    """
    
    """
    def __init__(self):
        self.__root = Tk()
        self.__root.title("PokiBooks")
        images = pkgutil.get_data( 'images', 'icon.png' )
        icon_data = pkgutil.get_data('icon', 'icon.ico')
        if icon_data == None:
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
            self.__root.attributes("-zoomed", True)  # This works on some Unix systems (like Linux)
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)
        self.current_book = None

        self.book_path = 'books/'
        self.cache_path = 'cache.json'

        if not os.path.exists(self.book_path):
            os.makedirs(self.book_path)

    # Frames and textscrollcombos
        self.text_container = make_full_frame(self.__root)

        self.text_frame = TextScrollCombo(self.text_container, bg=COLOR)
        self.text_frame.grid(column=0, row=0, sticky="nsew")

        self.all_books_menu = TextScrollCombo(self.text_container, bg=COLOR)

        # Change to textscrollcombo?
        self.sidebar = Frame(self.text_container, bg=COLOR, highlightthickness=1)
        self.sidebar.grid(column=1, row=0, sticky="ens")

    # Menus
        #Main Menus
        self.menubar       = make_main_menu(menubar=self.__root, bg=COLOR)
        self.settings_menu = make_main_menu(menubar=self.menubar, bg=BUTTON_COLOR)
        self.books_menu    = make_main_menu(menubar=self.menubar, bg=BUTTON_COLOR)
        self.help_menu     = make_main_menu(menubar=self.menubar, bg=BUTTON_COLOR)

        # Settings
        self.settings_menu.add_command(label="Fullscreen", command=self.fullscreen)
        self.settings_menu.add_separator()

        self.settings_menu.add_command(label='Set default theme', command=self.not_implemented)
        self.settings_menu.add_command(label="Toggle Sidebar", command=self.toggle_sidebar)
        self.settings_menu.add_separator()
        self.settings_menu.add_command(label="Exit", command=self._quit)

        # Book menu
        self.books_menu.add_command(label="Go to all books", command=self.go_to_books)
        self.books_menu.add_separator()
        self.books_menu.add_command(label="Clear Text", command=self.clear_text_frame)
        self.books_menu.add_command(label="Clear Cache", command=self.clear_cache)
        self.books_menu.add_command(label="Add book", command=self.add_book)
        self.books_menu.add_command(label="Remove book", command=self.remove_book)

        # Help Menu
        self.help_menu.add_command(label="Contact", command=self.not_implemented)
        self.help_menu.add_command(label="About", command=partial(info, self))

        # Menubar
        self.menubar.add_cascade(label="Settings", menu=self.settings_menu)
        self.menubar.add_cascade(label="Books", menu=self.books_menu)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        self.__root.config(menu=self.menubar)

    # Buttons
        self.all_books_button  = basic_button(self.sidebar, 'All Books', self.go_to_books)
        self.add_n_read_button = basic_button(self.sidebar, 'Add n\' Read Book', self.add_and_open)
        self.refresh_button    = basic_button(self.sidebar, 'Refresh', self.check_entries)
        self.ph                = basic_button(self.sidebar, 'Placeholder Button', self._quit)

        self.all_books_button.pack(side='top', fill='x')
        self.add_n_read_button.pack(side='top', fill='x', pady=10)
        self.refresh_button.pack(side='top', fill='x')
        self.ph.pack(side='top', fill='x', pady=10)

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
        self.center_var = tk.BooleanVar()
        self.center = Checkbutton(
            self.sidebar, bg=COLOR,
            highlightthickness=0,
            command=self.center_text,
            text='Center text',
            font=(FONT, FONT_SIZE),
            fg=FONT_COLOR,
            variable=self.center_var
            )
        self.center.pack(side='top', fill='x', pady=10)

    # Notes
        self.notebook = NoteBook(self.sidebar, self.cache_path)
        self.notes_button = Button(
            self.sidebar,
            text='Notebook',
            bg=BUTTON_COLOR,
            command=self.notebook.toggle,
            highlightthickness=0,
            font=(FONT, FONT_SIZE)
            )
        self.notes_button.pack(side='top', fill='x')
        
    # Themes
        self.themes_button = Menu(self.__root, tearoff=0, bg=BUTTON_COLOR, font=(FONT, FONT_SIZE))
        i = 0
        themes = AllThemes().get_all_themes()
        for theme in themes:
            theme.add(self, i)
            i += 1
        self.menubar.add_cascade(label="Themes", menu=self.themes_button)

        self.make_cache()

        self.__root.mainloop()

    def make_cache(self): # Returns: None
        """
        Make cache.json file 
        """
        if not os.path.exists(self.cache_path):
            with open(self.cache_path, 'w', encoding="utf-8") as file:
                json.dump({'books': {'notes': ''}}, file, indent=4)
                file.close()

    def clear_cache(self):
        os.remove(self.cache_path)
        if not os.path.exists(self.cache_path):
            with open(self.cache_path, 'w', encoding="utf-8") as file:
                json.dump({'books': {'notes': ''}}, file, indent=4)

    # cache book info
    def cache_book(self):
        # redo
        data = None
        with open(self.cache_path, 'r+', encoding="utf-8") as file:
            data = json.load(file)

        notes = self.notebook.text.get("1.0", 'end')
        if self.current_book is not None:

            if self.current_book not in data['books']:
                data['books'][self.current_book] = {}

            data['books'][self.current_book]['scrollbar'] = self.text_frame.scrollb.get()

            if notes != '':
                data['books'][self.current_book]['notes'] = notes
        else:
            if notes != '':
                data['books']['notes'] = notes

        with open(self.cache_path, 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            file.close()
    
    def remove_book(self): # Returns: None
        """
        Not implemented
        """
        return NotImplemented

    def add_and_open(self): # Returns: None
        """
        Add book and open to instantly read
        """
        path = self.add_book()
        if path:
            self.read_book(self.book_path + path.split('/')[-1])

    def add_book(self): # Returns: str 
        """
        Add book from filedialog. Returns book path
        """
        path = filedialog.askopenfilename(initialdir = str(Path.home() / "Downloads"))
        if path:
            try:
                shutil.move(path, self.book_path)
            except Exception as e:
                print(e)
            return path

    def clear_text_frame(self):
        self.text_frame = TextScrollCombo(self.text_container)
        self.text_frame.txt.config(bg=COLOR, fg=FONT_COLOR, font=(FONT, HEADING_SIZE))
        self.text_frame.grid(column=0, row=0, sticky="nsew")

    def go_to_books(self):
        self.text_frame.grid_forget()
        self.all_books_menu.txt = Frame(self.all_books_menu, bg=COLOR)
        self.all_books_menu.txt.grid(row=0, column=0, sticky='nsew')
        self.all_books_menu.grid(column=0, row=0, sticky="nsew")
        i = 0
        j = 0
        for file in os.scandir(self.book_path):
            if  i % 6 == 0:
                j += 1
                i = 0
            txt = file.name.split('.')[0].replace('_', ' ').capitalize()
            path = self.book_path + file.name
            button = Button(
                self.all_books_menu.txt,
                text=f'{txt}',
                bg=BUTTON_COLOR,
                font=(FONT, HEADING_SIZE),
                fg=FONT_COLOR,
                activebackground=ACTIVE_BACKGROUND,
                activeforeground=ACTIVE_FONT,
                command=partial(self.read_book, path),
                width=16
                )
            button.grid(row=j, column=i, sticky='n', pady=10, padx=20)
            i += 1

    # open book
    def read_book(self, path):
        self.cache_book()
        self.current_book = path
        self.notebook.change_book(self.current_book)

        self.clear_text_frame()
        self.check_entries()
        self.all_books_menu.grid_forget()
        self.text_frame.grid(column=0, row=0, sticky="nsew")
        self.notebook.update()

        with open(path, 'r') as file:
            self.text_frame.insert(file.read())
        self.text_frame.txt.config(state='disabled')
        self.text_frame.set_scrollbar(path)

    # Enter fullscreen
    def fullscreen(self):
        self.__root.attributes("-fullscreen", True)
        self.__root.bind("<Escape>", lambda x: self.__root.attributes("-fullscreen", False))

    # change theme 
    def change_theme(
            self,
            color=COLOR,
            font_color=FONT_COLOR,
            button_color=BUTTON_COLOR,
            active_background=ACTIVE_BACKGROUND,
            active_font=ACTIVE_FONT,
            font=FONT,
            font_size=FONT_SIZE,
            heading_size=HEADING_SIZE
            ):
        COLOR             = color
        FONT_COLOR        = font_color
        BUTTON_COLOR      = button_color
        ACTIVE_BACKGROUND = active_background
        ACTIVE_FONT       = active_font
        FONT              = font
        FONT_SIZE         = font_size
        HEADING_SIZE      = heading_size

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
        self.sidebar.config(bg=COLOR)
        self.text_frame.config(bg=COLOR)
        self.menubar.config(activebackground=ACTIVE_BACKGROUND, activeforeground=ACTIVE_FONT)


        self.settings_menu.config(activebackground=ACTIVE_BACKGROUND, activeforeground=ACTIVE_FONT)
        self.books_menu.config(activebackground=ACTIVE_BACKGROUND, activeforeground=ACTIVE_FONT)
        self.help_menu.config(activebackground=ACTIVE_BACKGROUND, activeforeground=ACTIVE_FONT)
        self.themes_button.config(activebackground=ACTIVE_BACKGROUND, activeforeground=ACTIVE_FONT)

        for frame in frames:
            for widget in frame.winfo_children():
                try:
                    widget.config(bg=COLOR)
                except Exception as e:
                    if 'unknown option' not in str(e):
                        print(e)

                try:
                    widget.config(fg=FONT_COLOR)
                except Exception as e:
                    if 'unknown option' not in str(e):
                        print(e)

                if isinstance(widget, Checkbutton):
                    widget.config(activebackground=COLOR, activeforeground=ACTIVE_FONT)

                elif isinstance(widget, Button):
                    widget.config(bg=BUTTON_COLOR, activebackground=ACTIVE_BACKGROUND, activeforeground=ACTIVE_FONT)

                elif isinstance(widget, Entry):
                    widget.config(bg=BUTTON_COLOR)

                widget.update()

    def check_entries(self): # Returns: None
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

    def change_padx(self): # Returns: None
        """
        Change padding in x direction in text_frame TextScrollCombo
        """
        self.text_frame.txt.config(padx=self.padding_entry.get())

    def change_text_size(self): # Returns: None
        """
        Changes text size to number from entry TODO: add edgecases/errorhandling
        """
        self.text_frame.txt.configure(font=(FONT, self.text_size_entry.get()))

    def center_text(self): # Returns: None
        """
        Centers text in main text frame in book_frame textscrollcombo
        """
        if self.center_var.get():
            self.text_frame.txt.tag_configure("center", justify='center')
            self.text_frame.txt.tag_add("center", "1.0", "end")
        else:
            self.text_frame.txt.tag_delete('center')
        self.text_frame.grid()

    def toggle_sidebar(self): # Returns: None
        """
        Toggles sidebar
        """
        if self.sidebar.winfo_viewable():
            self.sidebar.grid_remove()
        else:
            self.sidebar.grid()

    def _quit(self): # Returns: None
        """
        Quit as intended
        """
        self.cache_book()
        self.__root.quit()
        self.__root.destroy()

    def not_implemented(self):
        """TODO: Add not implemented error"""
        return NotImplemented
