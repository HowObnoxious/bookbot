main.py

import sys
from stats import (
    words_in_string,
    character_count,
    sort_characters)


def args():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    report_formatting(file_path)

def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def report_formatting(file_path):

    text = get_book_text(file_path)
    characters = sort_characters(character_count(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    words_in_string(text)
    print("--------- Character Count -------")

    for entry in characters:
        print(f"{entry["char"]}: {entry["num"]}")

args()