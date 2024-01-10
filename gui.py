import tkinter as tk 

from tkinter import Canvas, Frame, Button, Tk, Text, ttk
import os

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__running = False
        self.__root.bg = 'white'
        self.__root.title("BookBot")
        self.__root.configure(background='white')
        self.__root.protocol("WM_DELETE_WINDOW", self._quit)
        self.__root.attributes('-zoomed', True)
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)

        # Frames
        self.text_frame = Frame(self.__root, bg='white')
        self.text_frame.grid(column=0, row=0, sticky="nsew")
        
        self.option_frame = Frame(self.__root, bg='white')
        self.option_frame.grid(column=1, row=0, sticky="ens")
        
        
        # Buttons and labels:
        self.frankenstein_button = Button(self.option_frame, text='Read Frankenstein', bg='lavender', command=self.frankenstein)
        self.frankenstein_button.pack(side="top", fill="x", pady=10)

        self.combo = TextScrollCombo(self.__root)

        self.combo.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.combo.txt.config(borderwidth=3, relief="sunken")

        style = ttk.Style()
        style.theme_use('clam')

        
        self.__root.mainloop()

    
    def frankenstein(self):
        if os.path.exists('books/frankenstein.txt'):
            with open('books/frankenstein.txt', 'r') as file:
                text = Text(self.text_frame, font=('Times New Roman', 15), highlightthickness=0, borderwidth=0)
                self.combo.insert(file.read())               


    def _quit(self):
        # Force quits, error: _tkinter.TclError: invalid command name ".!frame.!canvas"
        if os.path.exists('cache.txt'):
            os.remove('cache.txt')
        self.__running = False
        self.__root.quit()
        self.__root.destroy()

    def redraw(self):
        # Updates the screen to match whats happening
        self.__root.update_idletasks()
        self.__root.update()

class TextScrollCombo(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # ensure a consistent GUI size
        self.grid_propagate(False)
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    # create a Text widget
        self.txt = tk.Text(self)

    # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set
    
    def insert(self, text):
        self.txt.insert('insert', text)
        self.pack(side="top", fill='both', pady=10, expand=True, padx=30)
