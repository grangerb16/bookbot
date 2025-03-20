def count_words(text):
    return(len(text.split()))

def count_chars(text):
    bow = {}
    for char in list(text.lower()):
        bow[char] = bow.get(char, 0) + 1
    return bow