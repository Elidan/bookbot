def count_words_in_text(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def count_intances_of_characters(string):
    lowercase_string = string.lower()
    char_count = {}

    for l in lowercase_string:
        if (l not in char_count):
            char_count[l] = 1
        else:
            char_count[l] += 1
    
    return char_count

def sort_character_dictionary(dictionary):
    chars_list = []
    for char, count in dictionary.items():
        chars_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list