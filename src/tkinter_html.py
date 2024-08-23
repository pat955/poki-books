import re
from bs4 import BeautifulSoup

def parse_html(text_frame, text):
    soup = BeautifulSoup(text, 'html.parser')
    # tags = ['h1', 'italic', 'bold']
    # add title
    try:
        insert(text_frame, title(soup), 'h1')
    except AttributeError:
        print('No title error')
    body = soup.find_all('p')
    for paragraph in body:
        append(text_frame, paragraph.string.extract())



def title(soup):
   return soup.title.string.extract()


def insert(text_frame, text, tag=None):
    text_frame.txt.write(text, tag)

def append(text_frame, text, tag=None):
    text_frame.txt.append(text, tag=tag, add_newline=True)
