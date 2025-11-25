from stats import (
    get_num_words, 
    number_of_single_chars, 
    sort_chars, 
    report, 
)
import sys

def main():
    if (len(sys.argv) < 2 or len(sys.argv) > 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    report(filepath)

   
main()