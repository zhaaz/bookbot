def get_num_words(text):
    return len(text.split())

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def number_of_single_chars(text):
    # Suchen welche Chars vorhanden sind und Set bauen
    text = text.lower()
    unique_chars = set()
    for char in text: 
        if char not in unique_chars:
            unique_chars.add(char)

    # Chars zählen
    char_count = {}
    for char in unique_chars:
        char_count[char] = text.count(char)

    return char_count

def sort_chars(char_count):
    sorted_chars = []
    # [{"char" : "e", "num": 32}, {}, ...]
    for char in char_count:
        new_entry = {"char": char, "num": char_count[char]}
        sorted_chars.append(new_entry)

    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars


def sort_on(items):
    return items["num"]


def report(filepath):
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_count = number_of_single_chars(text)
    sorted_chars = sort_chars(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for pairs in sorted_chars:
        if pairs["char"].isalpha():
            print(f"{pairs["char"]}: {pairs["num"]}")

    print("============= END ===============")

