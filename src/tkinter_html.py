"""
-- tkinter_html.py --
html rendering for textframe
"""
import tkinter
from bs4 import BeautifulSoup
from basics import prettify_title


def parse_html(path: str, text_frame: tkinter.Frame, text: str) -> None:
    """
    TODO: improve this
    makes a soup with bs4, inserts title with heading1 tag.
    Then calls recurssive function contents_r
    """
    soup = BeautifulSoup(text, 'html.parser')
    insert(text_frame, extract_title(path, soup), 'h1')

    contents_r(text_frame, soup)

def contents_r(text_frame: tkinter.Frame, soup: BeautifulSoup) -> None:
    """
    TODO: improve this
    """
    for tag in soup.find_all():
        try:
            append(text_frame, tag.string.extract())
        except TypeError:
            contents_r(text_frame, tag)
        except AttributeError:
            try:
                contents_r(text_frame, tag)
            except Exception as e:
                print(e)
                continue


def extract_title(path: str, soup: BeautifulSoup) -> str:
    """
    Retuns title if possible from soup
    """
    try:
        title = soup.title.string.extract()
    except AttributeError:
        title = prettify_title(path)
    return title


def insert(text_frame: tkinter.Frame, text: str, tag: str = None) -> None:
    """
    insert text
    """
    text_frame.txt.write(text, tag)


def append(text_frame: tkinter.Frame, text: str, tag: str = None) -> None:
    """
    appends text with tag
    """
    text_frame.txt.append(text, tag=tag, add_newline=True)
