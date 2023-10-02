def main():
    frank_path = 'books/frankenstein.txt'
    print(count_characters(frank_path))
    #print(count_words(frank_path))
    #print(get_book_text(frank_path))

def get_book_text(path):
    book = open(path, 'r')
    return book.read()

def count_words(path):
    book_text = get_book_text(path)
    return len(book_text.split(' '))

def count_characters(path):
    count_dict = {}
    book_text = get_book_text(path)

    for i in book_text:
      
        if i.isalpha():
            i = i.lower()
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        else:
            if i in count_dict:
                count_dict[i] += 1 
            else:
                count_dict[i] = 1  

            

    return count_dict


def report(path):
    pass

main()