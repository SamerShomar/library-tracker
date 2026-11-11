import json

BOOKS_FILE = "books.json"


def print_banner():
    print("=== Library Tracker ===")


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
        
def print_banner():
    print("=== Library Tracker ===")
    print("Version 1.0 - by Samer")


def main():
    print_banner()
    list_books()


if __name__ == "__main__":
    main()