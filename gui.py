import tkinter as tk 

from tkinter import Canvas, Frame, Button, Tk, Text, ttk, Checkbutton, Entry, Label
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
        self.text_frame = TextScrollCombo(self.__root, bg='lavender')
        self.text_frame.grid(column=0, row=0, sticky="nsew")
        
        self.option_frame = Frame(self.__root, bg='white')
        self.option_frame.grid(column=1, row=0, sticky="ens")
        
        # Buttons and labels:
        self.frankenstein_button = Button(self.option_frame, text='Read Frankenstein', bg='lavender', command=self.frankenstein)
        self.frankenstein_button.pack(side="top", fill="x", pady=10)

        self.pap_button = Button(self.option_frame, text='Read Pride and Prejudice', bg='lavender', command=self.pride_and_prejudice)
        self.pap_button.pack(side="top", fill="x")

        self.__root.mainloop()

    
    def frankenstein(self):
        self.clear_text()
        if os.path.exists('books/frankenstein.txt'):
            with open('books/frankenstein.txt', 'r') as file:
                for line in file:
                    self.text_frame.insert(line)      
                

    def pride_and_prejudice(self):
        self.clear_text()
        if os.path.exists('books/pap.txt'):
            with open('books/pap.txt', 'r') as file:
                for line in file:
                    self.text_frame.insert(line)    


    def clear_text(self):
        self.text_frame.txt.delete('1.0', 'end')
        

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


class TextScrollCombo(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.config (bg = 'lavender', bd=0, highlightthickness=0)
    
    # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
    # create a Text widget
        self.txt = tk.Text(self)
        self.txt.config(font=('Times New Roman', 15), highlightthickness=0, borderwidth=0, padx=10, pady=10, wrap='word', relief='sunken')

    # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set
    

    def insert(self, text):
        self.txt.insert('insert', text)
        self.txt.grid(row=0, column=0, sticky='nsew')
        #self.pack(side="top", fill='both', pady=10, expand=True, padx=30)
