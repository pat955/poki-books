import re

def get_extension(path: str) -> str | None:
    """
    Returns file extension or None. Format: 'mobi', 'txt', ...
    """
    ext = re.search(r'\.(\w*?)$', path)
    if not ext:
        return None
    return ext.group(1)