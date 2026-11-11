import json

BOOKS_FILE = "books.json"


def print_banner():
    print("=" * 32)
    print("  Library Tracker - Search & Remove")
    print("=" * 32)


def search_books(books, query):
    """Return books whose title or author contains the query."""
    query = query.strip().lower()
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


def search_remove_menu(books):
    while True:
        print("\n1. Search books")
        print("2. Remove a book")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            results = search_books(books, input("Search for: "))
            if results:
                for book in results:
                    print(f"- {book['title']} by {book['author']}")
            else:
                print("No books found.")
        elif choice == "2":
            if remove_book(books, input("Title to remove: ")):
                print("Book removed.")
            else:
                print("Book not found.")
        elif choice == "3":
            break
        else:
            print("Invalid option.")


def main():
    print_banner()
    try:
        with open(BOOKS_FILE, encoding="utf-8") as f:
            books = json.load(f)
    except FileNotFoundError:
        books = []

    search_remove_menu(books)

    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=2)


if __name__ == "__main__":
    main()