def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    content = get_book_text("books/frankenstein.txt")
    print(content)


main()
