import re
from nltk import tokenize
from gui import Window

def main():
    #print('Put all text files in bookbot folder before starting program.')
    #book_path = input('Name of book with (ex. frankenstein.txt): ')
    win = Window(900, 900)
    book_path = 'books/frankenstein.txt'

    #print('Top 10 most used words:')
    #for word, value in most_used_words(book_path, 10).items():
        #print(f'{word} '+ '-'*(7-len(word))+f'was found {value} times!')

    #print(report(book_path))
    # print(count_words(frank_path))
    # print(get_book_text(frank_path))


def give_bookpath_name(path):
    pass 


def add_book_to_folder(path):
    pass 


def get_list_of_books():
    print(os.searchdir('books/')) 


def get_book_text(path):
    book = open(path, 'r')
    return book.read()


def count_words(path):
    book_text = get_book_text(path)
    return len(book_text.split(' '))


def count_characters(path):
    count_dict = {}
    book_text = get_book_text(path)

    for word in book_text:
        if word.isalpha():
            if word.lower() not in count_dict:
                count_dict[word.lower()] = 0
            count_dict[word.lower()] += 1

        elif word == ' ' or word == '\t' or word == '\n':
            continue

        else:
            if word not in count_dict:
                count_dict[word] = 0 
            count_dict[word] += 1      
    return count_dict


def report(path):
    report_text = ('-'*10 + f'| Book report of {path} |---'+'-'*10+'\n'+ f'Total words: {count_words(path)}\n')

    sorted_chr_dict = dict(sorted(count_characters(path).items(), key=lambda item: item[1], reverse= True))
    filtered_dict = dict(filter(lambda item: item[0].isalpha(), sorted_chr_dict.items()))

    for character, amount in filtered_dict.items():
        report_text += ('-'*(10) + f'The character {character} appears {amount} times.'+'-'*(13 -len(str(amount)))+'\n')

    report_text += ('-'*15 +'| End of book report |'+ '-'*15)
    return report_text


def search(path, keyword):
    snt_with_keyword = {}
    line_num = 0
    text_in_sentences = tokenize.sent_tokenize(get_book_text(path))

    for sentence in text_in_sentences:
        line_num += 1

        for word in sentence.split(' '):
            
            word = word.strip(',\n ;:."[]()*\\@{}`\'12345679_=€$£&%#! ')

            if word.lower() == keyword.lower():
                
                snt_with_keyword[sentence] = line_num

    return snt_with_keyword


def get_wordlist(path):
    wordlist = {}
    
    for word in get_book_text(path).split(' '):
        word = word.strip(',\n ;:."[]()*\\@{}`\'12345679_=€$£&%#! ')
        if word == '':
            continue
        if word not in wordlist:
            wordlist[word] = 0
        wordlist[word] += 1
    return wordlist


def most_used_words(path, num):
    wordlist = get_wordlist(path)

    wordlist = dict(sorted(wordlist.items(), key=lambda item: item[1], reverse= True))
    top_words = {}
    count = 0

    for key, value in wordlist.items():
        if count == num:
            break 
        top_words[key] = value
        count += 1

    return top_words


main()