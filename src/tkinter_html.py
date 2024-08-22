import re
from bs4 import BeautifulSoup

def parse_html(text_frame, text):
    soup = BeautifulSoup(text, 'html.parser')
    text_frame.toggle_multiblock()
    for line in soup.contents:
        text_frame.insert_block(line)

   


