import html.parser
import mobi
from tika import parser
import html
from pypdf import PdfReader

def load_book(text_frame, path): # Returns: None
    ext = get_extension(path)
    text_frame.reset_text()

    if ext == 'txt':
        load_txt(text_frame, path)

    elif ext == 'mobi':
        load_mobi(text_frame, path)
    
    elif ext == 'html':
        load_html(text_frame, path)
    
    elif ext == 'pdf':
        load_pdf(text_frame, path)
    
    elif ext == 'epub':
        load_epub(text_frame, path)

    elif not supported(ext):
        return NotImplementedError
    
    else:
        print(path, 'unknown error')

    text_frame.update()
    text_frame.set_scrollbar(path)

def get_extension(path):
    "TODO: Improve with regex or add edgecases, this doesnt work: Fundamental-Accessibility-Tests-Basic-Functionality-v2.0.0"
    try:
        extension = path.split('.')[1]
        return extension
    
    except IndexError:
        return ''
    
    except Exception as e:
        print(e)

    return ''

def load_txt(text_frame, path):
    with open(path, 'r') as f:
        text_frame.insert(f.read())
        f.close()

def load_mobi(text_frame, path):
    "TODO: delete tempdir"
    tempdir, filepath = mobi.extract(path)
    load_book(text_frame, filepath)

def load_epub(text_frame, path):
    parsed = parser.from_file(path)
    text_frame.insert(parsed["content"])

def load_html(text_frame, path):
    p = html.parser.HTMLParser
     
    with open(path, 'r') as f:
        text_frame.insert(f.read())
        f.close()

def load_pdf(text_frame, path):
    reader = PdfReader(path)
    meta = reader.metadata
    if meta:
        if meta.title:
            text_frame.insert(meta.title)
        if meta.author:
            text_frame.append('by '+ meta.author+'\n', add_newline=True)   

    for page in reader.pages:
        text = page.extract_text()
        text_frame.append(text, add_space=False)

def supported(extension): # Returns: bool
    supported_type = ['txt', 'mobi']
    return extension in supported_type