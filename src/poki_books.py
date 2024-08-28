"""
-- poki_books.py --
Initializes window that starts the bookbot program
"""
import sqlite3
from window import BookBot


def main() -> None:
    con = sqlite3.connect("tutorial.db")
    BookBot()


main()
