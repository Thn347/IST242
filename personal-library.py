"""
Simple Personal Library Management System
Author: Thuan Nguyen
Date: 1/30
Version: 1.5
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


def add_book(library):
    """
    Add a new book, its author and publication year to the library
    """
    title = input("Enter book title: ").strip().title()
    if title in library:
        print(f"\"{title}\" already existed")
    else:
        author = input("Enter the book's author: ").strip().title()
        
        while True:
            year = input("Enter the publication year: ").strip()
            if year.isdigit():
                year_public = int(year)
                if year_public >= 1000:
                    break
                else:
                    print("Please put year that is >= 1000!")
            else:
                print("Invalid input. Number only")

        library[title] = {"author": author, "year": year_public}
        print(f"\"{title}\" added successfully")


def view_books(library):
    """
    Viewing all books, their author and publication year
    """
    if not library:
        print("There are no available books")
        return
    
    for title in sorted(library.keys()):
        info = library[title]
        print(f"{title} by {info['author']}, public in {info['year']}")
   

def search_book(library):
    """
    Searching for the books you want
    """
    title = input("Enter the book's title to search: ").strip().title()
    if title in library:
        info = library[title]
        print(f"Found \"{title}\" by {info["author"]} - {info["year"]}")
    else:
        print(f"\"{title}\" not found")


def delete_book(library):
    """
    Delete a book from the library
    """
    title = input("Enter the book's title to remove: ").strip().title()

    if title in library:
        del library[title]
        print(f"\"{title}\" removed successfully.")
    else:
        print(f"\"{title}\" not found!")


def main():
    """
    Main program that loops menu options
    """
    library = {} # library is initialized to be empty
    
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            view_books(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            delete_book(library)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice - try again")


if __name__ == "__main__":
    main()