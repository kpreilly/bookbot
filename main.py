#! /usr/bin/python3
import os
from stats import get_num_words, character_frequencies, ordered_frequencies
import sys


def get_book_text(book_path: str) -> str:
    with open(book_path, "r", encoding="utf-8") as f:
        return f.read()


def convert_path_to_usable_format(path: str) -> str:
    separator = "/" if os.name == "posix" else "\\"
    if separator in path:
        return path
    else:
        return path.replace("/" if separator == "\\" else "\\", separator)


def test_path(path: str) -> bool:
    # determine separator
    if os.path.exists(path):
        return True
    return False


def usage():
    print("Usage: python3 main.py <path_to_book>")


def main(path: str):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in ordered_frequencies(character_frequencies(text)):
        print(f"{item['character']}: {item['count']}")
    print("============ END ================")


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        usage()
        sys.exit(1)
    path = convert_path_to_usable_format(sys.argv[1])
    if not test_path(path):
        print(f"Error: File not found: {path}")
        usage()
        sys.exit(1)
    main(path)
