# PokiBooks
![code coverage badge](https://github.com/pat955/poki_books/actions/workflows/ci.yml/badge.svg)

This is PokiBooks, a simple and clean eReader. Read books from txt, pdf, mobi or epub files, keep notes for each book, as well as customize layout, appearance and font size.

## Why?
Originally, this started as a simple "count words in a text file" task, however i kept building on it until it became something i actually use!
The main reason i continued working on this project is because I love reading, but I didn't have an eReader I really liked.

# Download
Download latest release: [HERE](https://github.com/octo-org/octo-repo/releases/latest)

Remeber to choose the one based on your operating system!

Test it out with any book from [Project Gutenberg](https://www.gutenberg.org/), it's is an archive of books available in the public domain. I recommend Frankenstein!
Remember, current supported formats are: **.txt, .pdf, .epub and .mobi**

# Quick Start From Terminal
### Clone project
```
git clone https://github.com/pat955/poki_books
```
### Download dependencies
Install pip and python if you haven't already
```
pip install -r ./requirements.txt
```
### Run Script
```
./scripts/run.sh
```
or alternatively 
```
python ./src/poki_books.py
```

# Usage 
* Supported formats: .txt, .epub, .mobi, .pdf, .html(still need to improve html)
* Upload books
* Read books and texts
* Saves your scrollbar position for each book so you avoid scrolling forever each time
* Take notes for each book 
* Themes
* Fullscreen
* Toggle sidebar
* Customize text size, padding and justification
  
# Plans
* Add Contact info and how to use section
* Pictures, maybe api gets book covers, goodreads API?
* Clean up code
* Add documentation
* Search 
* Bookmarking, highlights, saved over sessions 
* Keybinds
* Button back to top
* Page numbers?

## Done

* ePub support
* mobi support
* pdf support
* Logo
* Linux, windows & macOs release
* Better name
* Themes with fonts and font sizes
* More themes, especially some that strain your eyes less

Python version: 3.10.12

