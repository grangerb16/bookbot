import sys

def get_book_text(path):
    contents = ""
    with open(path) as file:
        contents = file.read()
    return contents

from stats import count_words
from stats import count_chars
from stats import sorted_dict_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(f"./{sys.argv[1]}")
    char_count_dict = count_chars(text)
    sorted_list = sorted_dict_list(char_count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f'{dict["char"]}: {dict["count"]}')
    print("============= END ===============")

main()