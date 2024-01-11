import tkinter as tk 
from functools import partial

from tkinter import Canvas, Frame, Button, Tk, Text, ttk, Checkbutton, Entry, Label, Radiobutton, Menu
from PIL import Image, ImageTk
import os
import json

# Colors are on light mode in book menu regardless of option selected
# Add notes for each book
# Add more themes
# Add drag and drop function
# Pictures
# Logo
# Add info
# Clean up code
# Add documentation
# Search
# Bookmark
# Highlight
# Make the cache useful now
# Keybinds
# Back to top button and stuff
# Page num?

COLOR = 'white'
FONT_COLOR = 'black'
BUTTON_COLOR = 'lavender'
FONT = 'Times New Roman'
FONT_SIZE1 = 12
FONT_SIZE2 = 15

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.bg = COLOR
        self.__root.title("BookBot")
        self.__root.configure(background=COLOR)
        self.__root.protocol("WM_DELETE_WINDOW", self._quit)
        self.__root.attributes('-zoomed', True)
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)
        self.current_book = None

        # Frames and textscrollcombos
        self.text_frame = TextScrollCombo(self.__root, bg=COLOR)
        self.text_frame.grid(column=0, row=0, sticky="nsew")

        self.books_menu = TextScrollCombo(self.__root, bg=COLOR)
        
        self.option_frame = Frame(self.__root, bg=COLOR)
        self.option_frame.grid(column=1, row=0, sticky="ens")
        
        # Menus
            #Main Menus
        self.menubar = Menu(self.__root, bg=COLOR, bd=1, font=(FONT, FONT_SIZE1))
        settings_menu = Menu(self.menubar, tearoff=0, bg=BUTTON_COLOR, font=(FONT, FONT_SIZE1))
        books_menu = Menu(self.menubar, tearoff=0, bg=BUTTON_COLOR, font=(FONT, FONT_SIZE1))
        helpmenu = Menu(self.menubar, tearoff=0, bg=BUTTON_COLOR, font=(FONT, FONT_SIZE1))

            #Settings
        settings_menu.add_command(label="Fullscreen", command=self.fullscreen)
        settings_menu.add_separator()
        settings_menu.add_command(label="Hide Sidebar", command=self.hide_sidebar)
        settings_menu.add_command(label="Show sidebar", command=self.show_sidebar)
        settings_menu.add_separator()
        settings_menu.add_command(label="Exit", command=self._quit)
        
            # Book menu
        books_menu.add_command(label="Go to all books", command=self.go_to_books)
        books_menu.add_separator()
        books_menu.add_command(label="Placeholder 1", command=self.donothing)
        books_menu.add_command(label="Placeholder 2", command=self.donothing)
        books_menu.add_command(label="Clear Cache", command=self.clear_cache)
        books_menu.add_command(label="Add book", command=self.donothing)
        books_menu.add_command(label="Remove book", command=self.donothing)

            # Help Menu
        helpmenu.add_command(label="Contact", command=self.donothing)
        helpmenu.add_command(label="About", command=self.donothing)

        self.menubar.add_cascade(label="Settings", menu=settings_menu)
        self.menubar.add_cascade(label="Books", menu=books_menu)
        self.menubar.add_cascade(label="Help", menu=helpmenu)

        self.__root.config(menu=self.menubar)

        # Buttons
        self.refresh_button = Button(self.option_frame, text='Refresh', bg=BUTTON_COLOR, command=self.check_entries, highlightthickness=0, font=(FONT, FONT_SIZE1))
        self.refresh_button.pack(side='top', fill='x')

        # Entries and Labels
        self.text_size_label = Label(self.option_frame, text='Text Size', bg=COLOR, font=(FONT, FONT_SIZE1))
        self.text_size_label.pack(side='top', fill='x', pady=5)

        self.text_size_entry = Entry(self.option_frame, bg=BUTTON_COLOR, highlightthickness=0)
        self.text_size_entry.pack(side="top", fill="x")

        #Themes
        self.light_theme = Radiobutton(self.option_frame, text="Light Theme", bg=COLOR, bd=0, value=1, highlightthickness=0, command=self.light_theme, anchor='w', font=(FONT, FONT_SIZE1))
        self.light_theme.pack(side="bottom", fill='x', padx=3)

        self.dark_theme = Radiobutton(self.option_frame, text="Dark Theme", bg=COLOR, bd=0, highlightthickness=0, value=2, command=self.dark_theme, anchor='w', font=(FONT, FONT_SIZE1))
        self.dark_theme.pack(side="bottom", fill='x', padx=3)

        self.pistacchio = Radiobutton(self.option_frame, text="Pistacchio Theme", bg=COLOR, bd=0, highlightthickness=0, value=3, command=self.pistacchio_theme, anchor='w', font=(FONT, FONT_SIZE1))
        self.pistacchio.pack(side="bottom", fill='x', padx=3)

        

        self.light_theme.select()

            
        if not os.path.exists('cache.json'):
            with open('cache.json', 'w') as file:
                json.dump({'books': {}}, file, indent=4)

        self.__root.mainloop()


    def go_to_books(self):
        self.text_frame.grid_forget()
        self.books_menu.txt = Frame(self.books_menu, bg=COLOR)
        self.books_menu.txt.grid(row=0, column=0, sticky='nsew')
        self.books_menu.grid(column=0, row=0, sticky="nsew")

        i = 0
        j = 0
        for file in os.scandir('books/'):
            if  i % 6 == 0:
                j += 1
                i = 0
            
            path =f'books/{file.name}'
            button = Button(self.books_menu.txt, text=f'{file.name.split('.')[0].replace('_', ' ').capitalize()}', bg=BUTTON_COLOR, font=(FONT, FONT_SIZE2), command=partial(self.read_book, path), width=16)
            button.grid(row=j, column=i, sticky='n', pady=10, padx=20)
            i += 1


    def clear_cache(self):
        os.remove('cache.json')
        if not os.path.exists('cache.json'):
            with open('cache.json', 'w') as file:
                json.dump({'books': {}}, file, indent=4)


    def save_current_book_position(self):
        if self.current_book is not None:
            file_data = None
            with open('cache.json', 'r+') as file:
                file_data = json.load(file)
                if self.current_book in file_data['books']:
                    file_data['books'][self.current_book].update(str(self.text_frame.scrollb.get()))

                else:
                    file_data['books'][self.current_book] = {'scrollbar': str(self.text_frame.scrollb.get())}

            
            with open('cache.json', 'w') as file:
                json.dump(file_data, file, indent=4)


    def read_book(self, path):
        self.save_current_book_position()
        self.current_book = path

        self.clear_text()
        self.check_entries()
        self.books_menu.grid_forget()
        self.text_frame.grid(column=0, row=0, sticky="nsew")
        with open(path, 'r') as file:
            for line in file:
                self.text_frame.insert(line)
    

    def fullscreen(self):
        self.__root.attributes("-fullscreen", True)
        self.__root.bind("<Escape>", lambda x: self.__root.attributes("-fullscreen", False))


    def hide_sidebar(self):
        self.option_frame.grid_forget()
    
    
    def show_sidebar(self):
        self.option_frame.grid(column=1, row=0, sticky="ens")


    def donothing():
        return


    def pistacchio_theme(self):
        self.change_theme('azure', 'gray5', 'DarkOliveGreen3')


    def dark_theme(self):
        self.change_theme('gray11', 'white', 'steel blue')


    def light_theme(self):
        self.change_theme('white', 'black', 'lavender')


    def change_theme(self, color, font_color, button_color):
        COLOR = color
        FONT_COLOR = font_color
        BUTTON_COLOR = button_color
        frames = [self.__root, self.option_frame, self.text_frame, self.menubar, self.books_menu, self.books_menu.txt]

        for frame in frames:
            for widget in frame.winfo_children():
                try:
                    widget.config(bg=COLOR)
                except:
                    pass

                if type(widget) in [Button, Entry]:
                    widget.config(bg=BUTTON_COLOR)
        
                try: 
                    widget.config(fg=FONT_COLOR)
                except Exception as e:
                    pass
        
        widget.update()
    
    
    def check_entries(self):
        entries = {
            self.text_size_entry: self.change_text_size
            }
        for entry, func in entries.items():
            if entry.get():
                func()


    def change_text_size(self):
        self.text_frame.txt.config(font=(FONT, self.text_size_entry.get()))


    def clear_text(self):
        self.text_frame.txt.delete('1.0', 'end')
        

    def _quit(self):
        self.__root.quit()
        self.__root.destroy()


    def redraw(self):
        # Updates the screen to match whats happening
        self.__root.update_idletasks()
        self.__root.update()


class TextScrollCombo(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
    # create a Text widget
        self.txt = tk.Text(self)
        self.txt.config(font=(FONT, FONT_SIZE2), highlightthickness=0, borderwidth=0, padx=10, pady=10, wrap='word', relief='sunken')

    # create a Scrollbar and associate it with txt
        self.scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set

    

    def insert(self, text):
        self.txt.insert('insert', text)
        self.txt.grid(row=0, column=0, sticky='nsew')
    