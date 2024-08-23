import random
from bs4 import BeautifulSoup

def parse_html(text_frame, text):
    soup = BeautifulSoup(text, 'html.parser')
    tags = ['h1', 'italic', 'bold']
    for line in soup.contents:
        for i in line:
            text_frame.txt.write(i, random.choice(tags))

   


