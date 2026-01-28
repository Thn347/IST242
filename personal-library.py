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

def add_book(library: list[str]):
    """
    Add a new book to the library list
    """
    title = input("Enter book title: ").strip()
    library.append(title)

    print(f"Added: {title}")


def view_books():
    """
    Docstring for view_books
    """


def search_book():
    """
    Docstring for search_book
    """


def delete_book():
    """
    Docstring for delete_book
    """


def main():
    """
    Main program that loops menu options
    """
    library: list[str] = [] # library is initialized to be empty

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice - try again")


if __name__ == "__main__":
    main()