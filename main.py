def get_book_text(path):
    contents = ""
    with open(path) as file:
        contents = file.read()
    return contents

from stats import count_words

from stats import count_chars

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(f'{count_words(text)} words found in the document')
    print(count_chars(text))

main()