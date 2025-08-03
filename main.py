import sys

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

from stats import word_count

from stats import character_count

from stats import dict_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print("'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)
    imported_book = get_book_text(sys.argv[1])
    words_in_text = word_count(imported_book)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {words_in_text} total words\n--------- Character Count -------")
    #dict_of_characters = character_count(imported_book)
    #print(dict_of_characters)
    sorted_dict = dict_to_sorted_list(character_count(imported_book))
    for char in sorted_dict:
        if char["char"].isalpha() == True:
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
main()