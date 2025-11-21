from stats import *
import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

bookpath = sys.argv[1]

def getbooktext(f):
    with open(f, 'r') as file:
        return file.read()

def main():
 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    num_words = get_num_words(getbooktext(bookpath))
    char_frequency = get_char_frequency(getbooktext(bookpath))
    sorted_char_frequency = create_sorted_dictionary(char_frequency)
    
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    for item in sorted_char_frequency:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    


if __name__ == "__main__":
    main()