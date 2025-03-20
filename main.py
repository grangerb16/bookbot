def get_book_text(path):
    contents = ""
    with open(path) as file:
        contents = file.read()
    return contents

def count_words(text):
    return(len(text.split()))

def main():
    print(f'{count_words(get_book_text("./books/frankenstein.txt"))} words found in the document')

main()