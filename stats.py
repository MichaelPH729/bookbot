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