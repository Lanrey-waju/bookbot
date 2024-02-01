def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = count_words(text)
    print(f"There are {num_of_words} words in this book.")


def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count


main()
