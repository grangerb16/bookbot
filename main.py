def get_book_text(path):
    contents = ""
    with open(path) as file:
        contents = file.read()
    return contents

from stats import count_words
from stats import count_chars
from stats import sorted_dict_list

def main():
    text = get_book_text("./books/frankenstein.txt")
    char_count_dict = count_chars(text)
    sorted_list = sorted_dict_list(char_count_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f'{dict["char"]}: {dict["count"]}')
    print("============= END ===============")

main()