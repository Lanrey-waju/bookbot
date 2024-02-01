def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = count_words(text)
    letter_count = count_letters(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count


def count_letters(text):
    count = {}
    for char in text.lower():
        if char in count:
            count[char] += 1
        else:
            count[char] = 0
    return count


main()
