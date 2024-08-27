"""
-- basics.py --
Collection of basic tkinter widgets and other basic functions
"""
import os
import tkinter
from tkinter import Button, Label, Entry, Frame, Menu
from defaults import *  # pylint: disable=W0401


def basic_button(root: Frame, name: str, command) -> Button:
    """
    Makes a very basic button with all the default colors and font info.
    """
    return Button(
        root,
        text=name,
        bg=BUTTON_COLOR,
        command=command,
        highlightthickness=0,
        font=(FONT, FONT_SIZE),
        activebackground=ACTIVE_BACKGROUND,
        activeforeground=ACTIVE_FONT
    )


def basic_label(root: Frame, name: str) -> Label:
    """
    Makes a very basic label with default background color, font and font size
    """
    return Label(root, text=name, bg=COLOR, font=(FONT, FONT_SIZE))


def basic_entry(root: Frame) -> Entry:
    """
    Makes a very basic entry with default button color as background
    """
    return Entry(root, bg=BUTTON_COLOR, highlightthickness=0)


def make_full_frame(root: Frame) -> Frame:
    """
    Returns a frame with "fullscreen" config
    """
    f = Frame(root)
    f.columnconfigure(0, weight=1)
    f.rowconfigure(0, weight=1)
    f.grid(column=0, row=0, sticky="nsew")
    return f


def make_basic_menu(menubar, bg: str) -> tkinter.Menu:
    """
    Returns a Menu object with default theme
    """
    return Menu(
        menubar,
        tearoff=0,
        bg=bg,
        font=(FONT, FONT_SIZE),
        activebackground=ACTIVE_BACKGROUND,
        activeforeground=ACTIVE_FONT
    )


def dir_empty(dir_path: str) -> bool:
    """
    Checks if directory is empty
    """
    return not any((True for _ in os.scandir(dir_path)))


def prettify_title(title: str) -> str:
    return title.split('.')[0].replace('_', ' ').capitalize()


def info(window: tkinter.Frame) -> None:
    """
    How to use and faq for bookbot
    """
    window.text_frame.show_error(
        'NotImplementedError',
        'No info yet, planning on adding user guide, readme type text and FAQ. Links to github as well. @pat955 at github')


def contact(window: tkinter.Frame) -> None:
    """
    TODO: Add contact info, link to other projects and stuff like that
    """
    window.text_frame.show_error('NotImplementedError', 'No contact info yet')
