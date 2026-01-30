import sys
from stats import count_words, count_characters, sort_characters

def get_book_test(filepath):
    """
    Input path to a book plain-text file
    To fetch the contents of the book and print as text
    """
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_test(book_path)
    word_count = 0
    if book_content:
        word_count = count_words(book_content)
        character_count_dict = count_characters(book_content)
        sorted_characters = sort_characters(character_count_dict)
        if sorted_characters:
            sorted_characters = "\n".join([f"{item['char']}: {item['num']}" for item in sorted_characters if item['char'].isalpha()])
    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{sorted_characters}
============= END ===============
    """)
    
    
    # print(f"Found {word_count} total words")
    # print(f"Characters {character_count}")
    #print(book_content)
main()
