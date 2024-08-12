import html.parser
import mobi
import epub
import html

def load_book(text_frame, path): # Returns: None
    ext = get_extension(path)
    text_frame.reset_text()

    if ext == 'txt':
        load_txt(text_frame, path)

    elif ext == 'mobi':
        load_mobi(text_frame, path)
    
    elif ext == 'html':
        load_html(text_frame, path)

    elif not supported(ext):
        return NotImplementedError
    
    else:
        print(path, 'unknown error')

    text_frame.update()
    text_frame.set_scrollbar(path)

def get_extension(path):
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

def load_epub(path):
    file = epub.open(path)
    print(str(file.read))
    file.close()

def load_html(text_frame, path):
    p = html.parser.HTMLParser
        
    with open(path, 'r') as f:
        text_frame.insert(f.read())
        f.close()

def supported(extension): # Returns: bool
    supported_type = ['txt', 'mobi']
    return extension in supported_type