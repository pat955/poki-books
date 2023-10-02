def main():
    frank_path = 'books/frankenstein.txt'
    print(count_words(frank_path))
    #print(get_book_text(frank_path))

def get_book_text(path):
    book = open(path, 'r')
    return book.read()

def count_words(path):
    book_text = get_book_text(path)
    count = 0 

    for word in book_text.split(' '):
        count += 1
        
    return count

main()