import json

BOOKS_FILE = "books.json"


def print_banner():
    print("=" * 32)
    print("  Library Tracker - Search & Remove")
    print("  Version 1.0")
    print("=" * 32)


def load_books():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=2)


def add_book(title, author):
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)


def list_books():
    for i, book in enumerate(load_books(), start=1):
        print(f"{i}. {book['title']} - {book['author']}")


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
    books = load_books()
    list_books()
    search_remove_menu(books)
    save_books(books)


if __name__ == "__main__":
    main()