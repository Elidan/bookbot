from stats import count_words_in_text
from stats import count_intances_of_characters
from stats import sort_character_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def checkSysInput(input):
    if len(input) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    #Validate input
    checkSysInput(sys.argv)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    book = get_book_text(f"{sys.argv[1]}")
    words = count_words_in_text(book)
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    character_count = count_intances_of_characters(book)
    sorted_list = sort_character_dictionary(character_count)
    for pair in sorted_list:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["count"]}")
    print("============= END ===============")

main()