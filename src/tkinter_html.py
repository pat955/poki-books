import random
from bs4 import BeautifulSoup

def parse_html(text_frame, text):
    soup = BeautifulSoup(text, 'html.parser')
    tags = ['big', 'medium', 'small']
    for line in soup.contents:
        text_frame.txt.write(line, random.choice(tags))

   


