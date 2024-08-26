"""
-- book_types.py --
Loads books based on extension/type
"""
import tkinter
import mobi
from tika import parser
from pypdf import PdfReader
from tkinter_html import parse_html


def load_book(text_frame: tkinter.Frame, path: str) -> None:
    """
    With extension, resets text frame and runs the function that the type corresponds to.
    Then updates frame, text and scrollbar.
    TODO error handeling
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
    # try:
    types[ext](text_frame, path)
    # except Exception as e:
    #     print(e)
    #     print(path, 'unknown error')
    #     return NotImplementedError

    text_frame.update()
    text_frame.set_scrollbar(path)


def get_extension(path: str) -> str:
    """
    TODO: Improve with regex or add edgecases,
    this doesnt work: Fundamental-Accessibility-Tests-Basic-Functionality-v2.0.0

    """

    try:
        extension = path.split('.')[1]
        return extension

    except IndexError:
        return ''

    except Exception as e:
        print(e)

    return ''


def load_txt(text_frame: tkinter.Frame, path: str) -> None:
    """
    TODO: test out print per line to make it quicker
    Loads a text file, alternatively simply inserts text if no special actions are needed.
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
    TODO: delete tempdir
    Loads .mobi, extracts the file then loads the extension. (Could be .epub, .pdf or .html)
    """
    _, filepath = mobi.extract(path)
    load_book(text_frame, filepath)


def load_epub(text_frame: tkinter.Frame, path: str) -> None:
    """
    TODO: tika
    Loads epub, only loads 'content'
    """
    parsed = parser.from_file(path)
    text_frame.insert_text(parsed["content"])


def load_html(text_frame: tkinter.Frame, path: str) -> None:
    """
    Loads html, runs parse_html function
    """
    with open(path, 'r') as f:
        parse_html(text_frame, f.read())

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
