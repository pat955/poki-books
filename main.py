def main():
    frank_path = 'books/frankenstein.txt'
    print(report(frank_path))
    # print(count_words(frank_path))
    # print(get_book_text(frank_path))

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
        elif i == ' ' or i == '\t' or i == '\n':
            continue
        else:
            if i in count_dict:
                count_dict[i] += 1 
            else:
                count_dict[i] = 1      

    return count_dict


def report(path):
    report_text = f'---| Book report of {path} |---\n'+ f'Total words: {count_words(path)}\n'

    sorted_chr_dict = dict(sorted(count_characters(path).items(), key=lambda item: item[1], reverse= True))
    filtered_dict = dict(filter(lambda item: item[0].isalpha(), sorted_chr_dict.items()))

    for character, amount in filtered_dict.items():
        report_text += (f'The character {character} appears {amount} times.\n')

    report_text += ('---| End of book report |---')
    return report_text

    
main()