def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_occurrence_dict(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_counts(count_dict):
    sorted_list = []
    for char in count_dict:
        sorted_list.append({ "char": char, "num": count_dict[char] })
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list