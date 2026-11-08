def print_banner():
    print("=== Library Tracker ===")


def search_books(books, query):
    """Return books whose title or author contains the query."""
    query = query.lower()
    return [
        book for book in books
        if query in book["title"].lower() or query in book["author"].lower()
    ]


def remove_book(books, title):
    """Remove the book with the given title. Return True if removed."""
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            return True
    return False


def main():
    print_banner()


if __name__ == "__main__":
    main()