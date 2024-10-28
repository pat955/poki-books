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
    Makes a soup with bs4, inserts title and content
    """
    soup = BeautifulSoup(text, 'html.parser')
    text_frame.insert_text(extract_title(path, soup), 'h1')
    contents_r(text_frame, soup)


def contents_r(text_frame: tkinter.Frame, soup: BeautifulSoup) -> None:
    """
    Recursively go through a html tree and renders content
    """
    for tag in soup.find_all():
        try:
            text_frame.append_text(tag.string.extract(), add_newline=True)
            text_frame.update_text()
        except TypeError:
            contents_r(text_frame, tag)
        except AttributeError:
            try:
                contents_r(text_frame, tag)
            except Exception as e:
                print(type(e))
                print('Unknown error: ' + e)
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
