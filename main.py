import sys

from stats import get_num_words, get_char_occurrence_dict, sort_counts

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main(book_path):
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_occurrences = get_char_occurrence_dict(book_text)
    sorted_counts = sort_counts(char_occurrences)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count in sorted_counts:
        if count["char"].isalpha():
            print(f'{count["char"]}: {count["num"]}')

if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    main(book_path)