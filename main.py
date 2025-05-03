from stats import get_word_count
from stats import get_char_count
from stats import char_count_sorted
#from stats import sort_on

def main():
    bookpath = "books/frankenstein.txt"
    file_contents = get_book_text(bookpath)
    num_words = get_word_count(file_contents)
    num_chars = get_char_count(file_contents)
    chars = char_count_sorted(num_chars)
    print_report(bookpath, num_words, chars)
    #print(f"{num_words} words found in the document")
    #print(chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(bookpath, num_words, chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in chars:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()

#def main():
#    book_path = "books/frankenstein.txt"
#    text = get_book_text(book_path)
#    num_words = get_num_words(text)
#    print(f"{num_words} words found in the document")


#def get_book_text(path):
#    with open(path) as f:
#        return f.read()


#def get_num_words(text):
#    words = text.split()
#    return len(words)


#main()
