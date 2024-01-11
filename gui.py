import tkinter as tk 

from tkinter import Canvas, Frame, Button, Tk, Text, ttk, Checkbutton, Entry, Label, Radiobutton, Menu
from PIL import Image, ImageTk
import os

COLOR = 'white'
FONT_COLOR = 'black'
BUTTON_COLOR = 'lavender'

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__running = False
        self.__root.bg = COLOR
        self.__root.title("BookBot")
        self.__root.configure(background=COLOR)
        self.__root.protocol("WM_DELETE_WINDOW", self._quit)
        self.__root.attributes('-zoomed', True)
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)

        # Frames
        self.text_frame = TextScrollCombo(self.__root, bg=COLOR)
        self.text_frame.grid(column=0, row=0, sticky="nsew")

        self.books_menu = TextScrollCombo(self.__root, bg=COLOR)
        
        
        self.option_frame = Frame(self.__root, bg=COLOR)
        self.option_frame.grid(column=1, row=0, sticky="ens")
        
        # Menus
        self.menubar = Menu(self.__root, bg=COLOR, bd=1)
        settings_menu = Menu(self.menubar, tearoff=0, bg=BUTTON_COLOR)
        settings_menu.add_command(label="Fullscreen", command=self.fullscreen)
        settings_menu.add_separator()
        settings_menu.add_command(label="Hide Sidebar", command=self.hide_sidebar)
        settings_menu.add_command(label="Show sidebar", command=self.show_sidebar)
        settings_menu.add_separator()
        settings_menu.add_command(label="Exit", command=self._quit)
        self.menubar.add_cascade(label="Settings", menu=settings_menu)

        books_menu = Menu(self.menubar, tearoff=0, bg=BUTTON_COLOR)
        books_menu.add_command(label="Go to book menu", command=self.go_to_books)
        books_menu.add_separator()
        books_menu.add_command(label="Frankenstein", command=self.frankenstein)
        books_menu.add_command(label="Pride and prejudice", command=self.pride_and_prejudice)

        books_menu.add_command(label="Previous book", command=self.donothing)
        books_menu.add_command(label="Add book", command=self.donothing)
        books_menu.add_command(label="Remove book", command=self.donothing)
        self.menubar.add_cascade(label="Books", menu=books_menu)

        helpmenu = Menu(self.menubar, tearoff=0, bg=BUTTON_COLOR)
        helpmenu.add_command(label="Contact", command=self.donothing)
        helpmenu.add_command(label="About", command=self.donothing)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
        

        self.__root.config(menu=self.menubar)

        # Buttons:
        self.frankenstein_button = Button(self.option_frame, text='Read Frankenstein', bg=BUTTON_COLOR, command=self.frankenstein, highlightthickness=0)
        self.frankenstein_button.pack(side="top", fill="x", pady=10)

        self.pap_button = Button(self.option_frame, text='Read Pride and Prejudice', bg=BUTTON_COLOR, command=self.pride_and_prejudice, highlightthickness=0)
        self.pap_button.pack(side="top", fill="x")

        self.refresh_button = Button(self.option_frame, text='Refresh', bg=BUTTON_COLOR, command=self.check_entries, highlightthickness=0)
        self.refresh_button.pack(side='top', fill='x', pady=10)

        # Entries and Labels
        self.text_size_label = Label(self.option_frame, text='Text Size', bg=COLOR)
        self.text_size_label.pack(side='top', fill='x', pady=5)

        self.text_size_entry = Entry(self.option_frame, bg=BUTTON_COLOR, highlightthickness=0)
        self.text_size_entry.pack(side="top", fill="x")

        #Themes
        self.light_theme = Radiobutton(self.option_frame, text="Light Theme", bg=COLOR, bd=0, value=1, highlightthickness=0, command=self.light_theme)
        self.light_theme.pack(side="bottom", fill='x', anchor='w', padx=3)

        self.dark_theme = Radiobutton(self.option_frame, text="Dark Theme", bg=COLOR, bd=0, highlightthickness=0, value=2, command=self.dark_theme)
        self.dark_theme.pack(side="bottom", fill='x', anchor='w', padx=3)

        self.pistacchio = Radiobutton(self.option_frame, text="Pistacchio Theme", bg=COLOR, bd=0, highlightthickness=0, value=3, command=self.pistacchio_theme)
        self.pistacchio.pack(side="bottom", fill='x', anchor='w', padx=3)

        self.light_theme.select()
        self.__root.mainloop()


    def go_to_books(self):
        self.text_frame.grid_forget()
        self.books_menu.config(bg='lavender')
        self.books_menu.grid(column=0, row=0, sticky="nsew")
        
       
        for file in os.scandir('books/'):
            
            path =f'books/{file.name}'
            label = Button(self.books_menu, text=f'{file.name.capitalize().split('.')[0]}', bg=COLOR, font=('Times New Roman', 15), command=(self.read_book(path)))
            label.grid(sticky='n', pady=10, padx=20)
            

    def read_book(self, path):
        self.clear_text()
        self.check_entries()
        with open(path, 'r') as file:
            for line in file:
                self.text_frame.insert(line) 
        self.books_menu.grid_forget()
        self.text_frame.grid(column=0, row=0, sticky="nsew") 


    def fullscreen(self):
        self.__root.attributes("-fullscreen", True)
        self.__root.bind("<Escape>", lambda x: self.__root.attributes("-fullscreen", False))


    def hide_sidebar(self):
        self.option_frame.grid_forget()
    
    
    def show_sidebar(self):
        self.option_frame.grid(column=1, row=0, sticky="ens")


    def donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()
        

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
        frames = [self.__root, self.option_frame, self.text_frame, self.menubar]

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
    

    def frankenstein(self):
        self.clear_text()
        self.check_entries()
        if os.path.exists('books/frankenstein.txt'):
            with open('books/frankenstein.txt', 'r') as file:
                for line in file:
                    self.text_frame.insert(line)      
                

    def pride_and_prejudice(self):
        self.clear_text()
        self.check_entries()
        if os.path.exists('books/pap.txt'):
            with open('books/pap.txt', 'r') as file:
                for line in file:
                    self.text_frame.insert(line)    
    
    
    def check_entries(self):
        entries = {
            self.text_size_entry: self.change_text_size
            }
        for entry, func in entries.items():
            if entry.get():
                func()


    def change_text_size(self):
        self.text_frame.txt.config(font=('Times New Roman', self.text_size_entry.get()))


    def clear_text(self):
        self.text_frame.txt.delete('1.0', 'end')
        

    def _quit(self):
        # Force quits, error: _tkinter.TclError: invalid command name ".!frame.!canvas"
        with open ('cache.txt', 'w') as file:
            # Add which book the position is for.
            file.write(str(self.text_frame.scrollb.get()))
        self.__running = False
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
        self.txt.config(font=('Times New Roman', 15), highlightthickness=0, borderwidth=0, padx=10, pady=10, wrap='word', relief='sunken')

    # create a Scrollbar and associate it with txt
        self.scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        self.scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = self.scrollb.set

    

    def insert(self, text):
        self.txt.insert('insert', text)
        self.txt.grid(row=0, column=0, sticky='nsew')