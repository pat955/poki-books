import re

def get_html_dict(text):
    d = {}
    html_to_dict(text, d)
    return d


def html_to_dict(text, html_dict, path=[]):
    print('here again')
    start_tag, content, end_tag, error = split_tags(text)

    if error is not None:
        # Traverse through the dictionary using the given path
        current_dict = html_dict
        for p in path:
            current_dict = current_dict.setdefault(p, {})
        # Add the text at the final position in the path
        current_dict[text] = text
        return html_dict

    # Add the current start-end tag pair to the path
    current_tag = f'{start_tag} | {end_tag}'
    path.append(current_tag)

    # Traverse through the dictionary to the correct position
    current_dict = html_dict
    for p in path[:-1]:  # Exclude the last item because we are about to add it
        current_dict = current_dict.setdefault(p, {})

    # Add a new dictionary at the current tag
    current_dict[path[-1]] = {}

    # Recursively call the function to process the inner content
    html_to_dict(content, html_dict, path)

    # Once processing is done for the current content, backtrack the path
    path.pop()

    return html_dict


def split_tags(text):
    try:
        start_tag, rest = list(filter(None, re.split(r'^<(.+|[[:blank:]]*)>', text, 1)))
        print(rest)
        try: 
            contents, end_tag = list(filter(None, re.split(r'<\/(\S+|[[:blank:]]*)>$', rest, 1)))
        except Exception as e:
            print(e, list(filter(None, re.split(r'<\/(\S+|[[:blank:]]*)>$', rest, 1))))
        return start_tag, contents, end_tag, None

    except Exception as error:
       return '', '', '', error
    
        
def sort_html(s):
    if re.match('<h1>.+?<\/h1>', s):
        return heading1(s)
    elif re.match('<p>.+?<\/p>', s):
        return heading1(s)
    else:
        return 'does not match heading1, '+ s

def heading1(s):
    print('heading')
    return s

def paragraph(s):
    print('para')
    return s.rstrip('<p>').lstrip('</p>')