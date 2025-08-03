def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def word_count(text):
    return len(text.split())

def main():
    print(f"{word_count(get_book_text("./books/frankenstein.txt"))} words found in the document")

main()