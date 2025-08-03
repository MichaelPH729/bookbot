def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

from stats import word_count

from stats import character_count

def main():
    imported_book = get_book_text("./books/frankenstein.txt")
    print(f"{word_count(imported_book)} words found in the document")
    dict_of_characters = character_count(imported_book)
    print(dict_of_characters)

main()