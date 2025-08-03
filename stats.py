def word_count(text):
    return len(text.split())

def character_count(text):
    character_dictionary = {}
    for char in list(text):
        if char.lower() in character_dictionary:
            character_dictionary[char.lower()] += 1
        else:
            character_dictionary[char.lower()] = 1
    return character_dictionary

def dict_to_sorted_list(dict):
    def extract_count(char):
        return char["num"]
    extracted_dict_list = []
    for char in dict:
        extracted_dict_list.append({"char" : char, "num": dict[char]})
    extracted_dict_list.sort(reverse=True, key=extract_count)
    return extracted_dict_list