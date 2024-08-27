"""
-- menu.py --
A separated libary for menu making instead of cluttering window module
TODO:
Add contact info
Add info, about, faq, markdown
"""
import tkinter
from tkinter import Menu
from defaults import FONT, FONT_SIZE, ACTIVE_BACKGROUND, ACTIVE_FONT


def make_main_menu(menubar, bg: str) -> tkinter.Menu:
    """ Returns a Menu object with default theme """
    return Menu(
        menubar,
        tearoff=0,
        bg=bg,
        font=(FONT, FONT_SIZE),
        activebackground=ACTIVE_BACKGROUND,
        activeforeground=ACTIVE_FONT
    )


def info(window: tkinter.Frame) -> None:
    """
    How to use and faq for bookbot
    """
    window.clear_text()
    # markdown_string = '# BookBot'
    window.text_frame.insert("Nothing here yet")


def contact() -> None:
    """
    TODO: Add contact info, link to other projects and stuff like that
    """
    return
