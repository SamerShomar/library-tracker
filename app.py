import json
BOOKS_FILE = "books.json"
def print_banner():
    print("=== Library Tracker ===")
def load_books():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:

Pc@DESKTOP-0T27T5B MINGW64 ~ (master)
$ cd library-tracker

Pc@DESKTOP-0T27T5B MINGW64 ~/library-tracker (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

Pc@DESKTOP-0T27T5B MINGW64 ~/library-tracker (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

Pc@DESKTOP-0T27T5B MINGW64 ~/library-tracker (main)
$ git log --oneline
01aacc6 (HEAD -> main, origin/main) feat(app): add initial app skeleton with banner
48cc759 docs: add README and .gitignore

Pc@DESKTOP-0T27T5B MINGW64 ~/library-tracker (main)
$ ls
README.md  app.py

Pc@DESKTOP-0T27T5B MINGW64 ~/library-tracker (main)
$ cd library-tracker
bash: cd: library-tracker: No such file or directory

Pc@DESKTOP-0T27T5B MINGW64 ~/library-tracker (main)
$ git pull
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 9 (delta 5), reused 9 (delta 5), pack-reused 0 (from 0)
Unpacking objects: 100% (9/9), 1.44 KiB | 12.00 KiB/s, done.
From https://github.com/SamerShomar/library-tracker
 * [new branch]      feature/search-remove -> origin/feature/search-remove
Already up to date.

Pc@DESKTOP-0T27T5B MINGW64 ~/library-tracker (main)
$ git switch -c feature/add-list-books
Switched to a new branch 'feature/add-list-books'

Pc@DESKTOP-0T27T5B MINGW64 ~/library-tracker (feature/add-list-books)
$ cat > app.py << 'EOF'
> import json
> BOOKS_FILE = "books.json"
> def print_banner():
>     print("=== Library Tracker ===")
> def load_books():
>     try:
>         with open(BOOKS_FILE, "r", encoding="utf-8") as f:
>             return json.load(f)
>     except FileNotFoundError:
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
def main():
    print_banner()
    list_books()
if __name__ == "__main__":
    main()
