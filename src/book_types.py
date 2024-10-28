"""
-- book_types.py --
Loads books based on extension/type
"""
import tkinter
import re
import io
import mobi
import ebooklib
import gopy.api

from tkinter import END
from PIL import Image, ImageTk
from ebooklib import epub
from pypdf import PdfReader
from bs4 import BeautifulSoup
from tkinter_html import parse_html, contents_r


def get_extension(path: str) -> str | None:
    """
    Returns file extension or None. Format: 'mobi', 'txt', ...
    """
    ext = re.search(r'\.(\w*?)$', path)
    if not ext:
        return None
    return ext.group(1)


def prepare_book(book: gopy.api.Book) -> tuple[gopy.api.Book, Exception]:
    """
    Returns book so it can be put into the database with all found info
    """
    path = book.Path
    ext = get_extension(path)
    book.Extension = ext
    types = {
        'txt': prepare_txt,
        'mobi': prepare_mobi,
        'html': prepare_txt,
        'pdf': prepare_pdf,
        'epub': prepare_epub,
        'csv': prepare_txt
    }
    try:
        book = types[ext](book)  # Initializes matching function to type

    except KeyError:
        return None, Exception(f'KeyError: Unsupported format "{ext}"')

    except Exception as e:
        return None, Exception(f'Exception: Error message "{e}"')

    return book, None


def prepare_txt(book: gopy.api.Book) -> gopy.api.Book:
    """
    Adds content to book object
    """
    with open(book.Path, 'r') as f:
        book.Content = f.read()
        f.close()
    return book


def prepare_mobi(book: gopy.api.Book) -> gopy.api.Book:
    """
    Extracts "inner book" from mobi then calls prepare book on that inner book
    """
    i, book.Path = mobi.extract(book.Path)
    print("mobi:" + i)
    return prepare_book(book)


def prepare_pdf(book: gopy.api.Book) -> gopy.api.Book:
    """
    Gets metadata, adds author, adds title if available
    Then extracts content and adds to book object
    """
    reader = PdfReader(book.Path)
    meta = reader.metadata
    if meta:
        if meta.title:
            book.Title = meta.title
        if meta.author:
            book.Author = meta.author

    content = ""
    for page in reader.pages:
        content += page.extract_text()
    book.Content = content
    return book


def prepare_epub(book: gopy.api.Book) -> gopy.api.Book:
    """
    Gets metadata, adds title if available
    Then extracts content and adds to book object
    """
    try:
        epub_obj = epub.read_epub(book.Path)
    except Exception as e:
        print(f"here1 {e}")
    try:
        e = epub_obj.get_metadata('DC', 'title')[0]
        print(e)
    except Exception as e:
        print(f"here2 {e}")
        return

    # tkinter will delete the image if it isn't global
    # global images
    # images = {}
    content = ""
    for item in epub_obj.get_items():
        # html converted to normal text
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            content += content_soup_r(soup)
            print(content)
    book.Content = content
    return book
    # # images :)
    # elif item.get_type() == ebooklib.ITEM_IMAGE:

    #     hex_data = item.get_content()
    #     image = Image.open(io.BytesIO(hex_data))
    #     tk_img = ImageTk.PhotoImage(image)

    #     images[tk_img] = text_frame.txt.index(END)
    #     text_frame.txt.image_create(
    #         text_frame.txt.index(END), image=tk_img)
    #     text_frame.update()


def content_soup_r(soup: BeautifulSoup) -> str:
    """
    Recurssive function to get all contents from html tree
    """
    content = ""
    for tag in soup.find_all():
        try:
            content += tag.string.extract()
        except TypeError:
            return content_soup_r(tag)
        except AttributeError:
            try:
                return content_soup_r(tag)
            except Exception as e:
                print(type(e))
                print(f'Unknown error: {e}')
                continue
    return content


# --- loads text onto tkinter frame directly without database ---

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
        text_frame.show_error('Exception',
                              f'Unknown error, error message "{e}"')
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
    TODO: remove {{}} from title (prettify title function?)
    TODO: add ITEM_COVER
    Inserts title from metadata, then adds every 'item'
    For some books, all the images show up first instead of in order.
    This means that all images show up first, and images are out of place
    """
    book = epub.read_epub(path)

    title = book.get_metadata('DC', 'title')
    text_frame.insert_text(title, 'h1')

    # tkinter will delete the image if it isn't global
    global images
    images = {}
    for item in book.get_items():
        # html converted to normal text
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            contents_r(text_frame, soup)

        # images :)
        elif item.get_type() == ebooklib.ITEM_IMAGE:

            hex_data = item.get_content()
            image = Image.open(io.BytesIO(hex_data))
            tk_img = ImageTk.PhotoImage(image)

            images[tk_img] = text_frame.txt.index(END)
            text_frame.txt.image_create(
                text_frame.txt.index(END), image=tk_img)
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
