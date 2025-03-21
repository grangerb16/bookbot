def count_words(text):
    return(len(text.split()))

def count_chars(text):
    bow = {}
    for char in list(text.lower()):
        bow[char] = bow.get(char, 0) + 1
    return bow

def sorted_dict_list(dict):
    sorted_list = []

    def sort_on(dict):
        return dict["count"]

    for key in dict:
        sorted_list.append({"char": key, "count": dict[key]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list  