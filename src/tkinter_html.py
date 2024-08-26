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
    contents_r(text_frame, soup)
    
def contents_r(text_frame, soup):
    print(soup.find_all())
    for tag in soup.find_all():
        try:
            append(text_frame, tag.string.extract())
        except TypeError:
            contents_r(text_frame, tag)
        except AttributeError as e:
            try:
                contents_r(text_frame, tag)
            except Exception as e:
                print(e)
                continue
    

def title(soup):
    return soup.title.string.extract()

def insert(text_frame, text, tag=None):
    text_frame.txt.write(text, tag)

def append(text_frame, text, tag=None):
    text_frame.txt.append(text, tag=tag, add_newline=True)
