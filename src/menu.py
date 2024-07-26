from tkinter import Menu
from defaults import FONT, FONT_SIZE, ACTIVE_BACKGROUND, ACTIVE_FONT

def make_main_menu(menubar, bg):
    return Menu(menubar, tearoff=0, bg=bg, font=(FONT, FONT_SIZE), activebackground=ACTIVE_BACKGROUND, activeforeground=ACTIVE_FONT)
