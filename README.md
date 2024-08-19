# PokiBooks
![code coverage badge](https://github.com/pat955/poki_books/actions/workflows/ci.yml/badge.svg)

This is PokiBooks, a simple and clean eReader. Read books from txt, pdf, mobi or epub files, keep notes for each book, as well as customize layout, appearance and font size.

## Why?
Originally, this started as a simple "count words in a text file" task, however i kept building on it until it became something i actually use!
The main reason i continued working on this project is because I love reading, but I didn't have an eReader I really liked.

# Download
Download latest release: [HERE](https://github.com/pat955/poki_books/releases/latest)

Remember to choose the one based on your operating system!

Test it out with any book from [Project Gutenberg](https://www.gutenberg.org/). Project Gutenberg is an archive of books available in the public domain free of charge. I recommend reading Frankenstein!
Current supported formats are: **.txt, .pdf, .epub and .mobi**

Alternatively, if you want to run the app through terminal, follow the steps in the [Contributing section](#Contributing)

# Features 
* Upload and read any .txt, pdf, mobi or epub file with ease!
* Current supported formats include .txt, .epub, .mobi, .pdf and .html(still needs improvement regarding html)
* Saves your scrollbar position for each book so you avoid scrolling forever each time
* Take notes for each book
* Customize appearance with themes, font size, justification and padding 
* Toggle fullscreen and sizebar 

# Contributing
Python version: 3.10.12
### Clone project
```bash
git clone https://github.com/pat955/poki_books
```
### Download dependencies
Install pip and python if you haven't already
```bash
pip install -r ./requirements.txt
```
### Run Script
```bash
./scripts/run.sh
```
or alternatively 
```bash
python ./src/poki_books.py
```
### Run the tests

```bash
go test ./...
```

### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.

# Plans
- [ ] Add contact info and how to use section
- [ ] Pictures, maybe api gets book covers, goodreads API?
- [ ] Clean up code, add documentation, better structure, fix bugs
- [ ] Search, bookmarking, highlighting
- [ ] Switch to sql db
- [ ] Keybinds, back to top button
- [ ] Page numbers for pdf or when available.
- [ ] Recognize chapters?

- [x] ePub, pdf & mobi support
- [x] Simple logo & better name
- [x] Linux, windows & macOs release
- [x] Themes with fonts and font sizes & more themes
