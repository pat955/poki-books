import re
from nltk import tokenize

def main():
    frank_path = 'books/frankenstein.txt'
    keyword = 'present'
    search_finds = search(frank_path, keyword)
    print(f'The word {keyword} was found here:')
    for sentence, instance in search_finds.items():
        print(f'{keyword.} was found here:\n{sentence}\nAt line {instance}.\n')

    # print(report(frank_path))
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

def search(path, keyword):
    snt_with_keyword = {}
    line_num = 0
    text_in_sentences = tokenize.sent_tokenize(get_book_text(path))

    for sentence in text_in_sentences:
        line_num += 1

        for word in sentence.split(' '):
            
            word = word.strip(',,\n ;:."[]()*\\n')

            if word.lower() == keyword.lower():
                
                snt_with_keyword[sentence] = line_num

     

    return snt_with_keyword


    
main()