"""
-- book_types.py --
Loads books based on extension/type
"""
import tkinter
import re
import io
from tkinter import END
from PIL import Image, ImageTk
import mobi

import ebooklib
from ebooklib import epub

from pypdf import PdfReader
from tkinter_html import parse_html
from bs4 import BeautifulSoup

def get_extension(path: str) -> str|None:
    """
    Returns file extension or None. Format: 'mobi', 'txt', ...
    """
    ext = re.search(r'\.(\w*?)$', path)
    if not ext:
        return None
    return ext.group(1)


def load_book(text_frame: tkinter.Frame, path: str) -> None:
    """
    After getting file extension,
    resets text frame and calls the function that the type corresponds to.
    Updates frame, text and scrollbar.
    """
    ext = get_extension(path)
    text_frame.reset()
    types = {
        'txt': load_txt,
        'mobi': load_mobi,
        'html': load_html,
        'pdf': load_pdf,
        'epub': load_epub,
        'csv': load_txt
    }
    try:
        types[ext](text_frame, path)

    except KeyError:
        text_frame.show_error('KeyError', f'Unsupported format "{ext}"')
        return

    except Exception as e:
        text_frame.show_error('Exception', f'Unknown error, error message "{e}"')
        return
        
    text_frame.update()
    text_frame.set_scrollbar(path)


def load_txt(text_frame: tkinter.Frame, path: str) -> None:
    """
    TODO: test out print per line to make it quicker
    Loads a text file
    """
    # with open(path, 'rb') as f:
    #     for line in f:
    #         text_frame.append(f.read())
    # f.close()
    with open(path, 'r') as f:
        text_frame.insert_text(f.read())
        f.close()


def load_mobi(text_frame: tkinter.Frame, path: str) -> None:
    """
    Loads .mobi, extracts the file then loads the extension. 
    (Could be .epub, .pdf or .html)
    """
    _, filepath = mobi.extract(path)
    load_book(text_frame, filepath)


def load_epub(text_frame: tkinter.Frame, path: str) -> None:
    """

    """
    book = epub.read_epub(path)
    title = book.get_metadata('DC', 'title')
   
    text_frame.insert_text(title, 'h1')
    global images
    images = {}
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            contents_r_updating(text_frame, soup)

        elif item.get_type() == ebooklib.ITEM_IMAGE:
            
            hex_data = item.get_content()
            image = Image.open(io.BytesIO(hex_data))
            tk_img = ImageTk.PhotoImage(image)

            images[tk_img] = text_frame.txt.index(END)
            text_frame.txt.image_create(text_frame.txt.index(END), image=tk_img)
            text_frame.update()

def load_html(text_frame: tkinter.Frame, path: str) -> None:
    """
    Loads html, runs parse_html function
    """
    with open(path, 'r') as f:
        parse_html(path, text_frame, f.read())

        f.close()


def load_pdf(text_frame: tkinter.Frame, path: str) -> None:
    """
    Loads .pdf, first extracts metadata. Renders title and author then each page
    """
    reader = PdfReader(path)
    meta = reader.metadata
    if meta:
        if meta.title:
            text_frame.insert_text(meta.title)
        if meta.author:
            text_frame.append_text(
                'by ' + meta.author + '\n\n',
                add_newline=True)

    for page in reader.pages:
        text = page.extract_text()
        text_frame.append_text(text, add_space=False)
