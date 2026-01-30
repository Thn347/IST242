"""
Simple Personal Library Management System
Author: Thuan Nguyen
Date: 1/28
Version: 1.0
"""


def show_menu():
    """
    Display the main menu options to the user
    """
    print("\nPersonal Library Menu")
    print("  1. Add Book")
    print("  2. View Books")
    print("  3. Search Book")
    print("  4. Delete Book")
    print("  5. Exit")


def add_book(library, titles):
    """
    Add a new book, its author and publication year to the library
    """
    title = input("Enter book title: ").strip().title()
    if title in library:
        print(f"\"{title}\" already existed")
    else:
        author = input("Enter the book's author: ").strip().title()
        year = input("Enter the publication year: ").strip()
        book = (title, author, year)
        library.append(book)
        titles.add(title)
        print(f"\"{title}\" added successfully")


def view_books(library):
    """
    Viewing all books, their author and publication year
    """
    if not library:
        print("There are no available books")
        return
    for title, author, year in sorted(library, key=lambda b: b[0]):
        print(f"{title} by {author}, public in {year}")
   

def search_book(library):
    """
    Searching for the books you want
    """
    title = input("Enter the book's title to search: ").strip().title()
    for book in library:
        if book[0] == title:
            print(f"Found {book[0]} - {book[1]} - {book[2]}")
            return
    print(f"\"{title}\" not found")


def delete_book(library, titles):
    """
    Delete a book from the library
    """
    title = input("Enter the book's title to remove: ").strip().title()
    for book in library:
        if book[0] == title:
            library.remove(book)
            titles.remove(title)
            print(f"\"{title}\" removed successfully.")
            return
    print(f"\"{title}\" not found!")


def main():
    """
    Main program that loops menu options
    """
    library = [] # library is initialized to be empty
    titles = set()
    
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_book(library, titles)
        elif choice == "2":
            view_books(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            delete_book(library, titles)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice - try again")


if __name__ == "__main__":
    main()