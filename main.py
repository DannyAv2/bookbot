import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]


from stats import count_words, count_characters, chars_dict_to_sorted_list
    
def get_book_text(book_path):
    with open(book_path) as f:
        text = f.read()
        return text
    
def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    sorted_list = chars_dict_to_sorted_list(num_characters)
    print_report(book_path, num_words, sorted_list)

def print_report(book_path, num_words, sorted_list):
    print('============= BOOKBOT ==============')
    print(f'Analyzing book found at {book_path}')
    print('------------ Word Count -----------')
    print(f'Found {num_words} total words.')
    print('---------- Character Count -----------')
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    

    print('============= END ============')
main()