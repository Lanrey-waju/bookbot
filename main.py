def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = count_words(text)
    letter_count = count_letters(text)
    print_report(letter_count, book_path, num_of_words)


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


def print_report(dic, path, word_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in this document")
    print("\n")
    list_of_chars = list(dic)
    list_of_chars.sort()
    for char in list_of_chars:
        if char.isalpha():
            print(f"The '{char}' character was found {dic[char]} times ")
    print("--- End report ---")


main()
