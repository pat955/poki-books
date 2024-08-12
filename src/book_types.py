import mobi
from clear import clear_text_frame

def get_extension(path):
    try:
        extension = path.split('.')[1]
        return extension
    except IndexError:
        return ''
    except Exception as e:
        print(e)
    return ''

def load_book(text_frame, text_container, path):
    with open(path, 'r') as f:
        text = f.read()
        text_frame.clear()
        text_frame.insert(str(text))
        text_frame.txt.get('0.0', 'end')
        # text_frame.insert(text)

def txt_book():
    pass

def mobi_book():
    pass

def epub_book():
    pass

def not_supported():
    pass