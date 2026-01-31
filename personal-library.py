"""
Simple Personal Library Management System
Author: Thuan Nguyen
Date: 1/31
Version: 2.0
"""


def show_menu():
    """
    Display the main menu options to the user
    """
    print("\nPersonal Library Menu")
    print("  1.Add Book")
    print("  2.View Books")
    print("  3.Search Book")
    print("  4.Delete Book")
    print("  5.Update Book")
    print("  6.Statistic")
    print("  7.Exit")


def add_book(library):
    """
    Add a new book, its author and publication year to the library
    """
    title = input("Enter book title: ").strip().title()
    if title in library:
        confirm = input("This title already exists. Do you want to update it (Y/N)? ").strip().upper()
        if confirm == "N":
            print("No changes were made. The existing book was kept!")
            return
    
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
    
    print("\nYour Books:") 
    for i, title in enumerate(sorted(library.keys()), start=1):
        info = library[title]
        print(f"   {i}. {title} - {info['author']}, public in {info['year']}")
   

def search_book(library):
    """
    Searching for the books you want with partial and case-insensitive ability
    """
    search = input("Enter the book's title to search: ").strip().lower()

    match = []
    for title, info in library.items():
        if search in title.lower():
            match.append((title, info))

    if not match:
        print("No matching books were found.")
        return

    print("\nSearch results: ")
    for i, (title, info) in enumerate(match, start=1):
        print(f"   {i}. \"{title}\" by {info['author']} - public in {info['year']}")


def delete_book(library):
    """
    Delete a book from the library
    """
    title = input("Enter the book's title to remove: ").strip().title()

    if title in library:
        del library[title]
        print(f"\"{title}\" removed successfully.")
    else:
        print(f"\"{title}\" not found! Try again: ")


def update_book(library):
    """
    Updating existing book
    """
    title = input("Enter the book's title to update: ").strip().title()

    if title not in library:
        print(f"\"{title}\" not found!")
        return
    else:
        info = library[title]
        print(f"Current information: {title} by {info['author']}, public in {info['year']}")
        print("Which one do you want to update?")
        print("  1.Author")
        print("  2.Publication year")
        print("  3.Both")
        print("  4.None")

        while True:
            updating = input("Choose your option: ").strip()

            if updating == "1":
                new_author = input("Enter the new update for author: ").strip().title()
                info['author'] = new_author
                print("Successfully updated")
                break

            elif updating == "2":
                while True:
                    new_year = input("Enter the new update for publication year: ").strip()
                    if new_year.isdigit():
                        new_public_year = int(new_year)
                        if new_public_year >= 1000:
                            info['year'] = new_public_year
                            print("Successfully updated")
                            break
                        else:
                            print("Please put year that is >= 1000!")
                    else:
                        print("Invalid input. Number only")
                break

            elif updating == "3":
                new_author = input("Enter the new update for author: ").strip().title()
                info['author'] = new_author
                while True:
                    new_year = input("Enter the new update for publication year: ").strip()
                    if new_year.isdigit():
                        new_public_year = int(new_year)
                        if new_public_year >= 1000:
                            info['year'] = new_public_year
                            print("Successfully updated")
                            break
                        else:
                            print("Please put year that is >= 1000!")
                    else:
                        print("Invalid input. Number only")
                break

            elif updating == "4":
                print("No change made! See you again!")
                return
            
            else:
                print("Invalid choice - try again")


def statistic(library):
    if not library:
        print("There are no available books")
        return
    
    authors = {}
    for info in library.values():
        author = info['author']
        authors[author] = authors.get(author, 0) + 1

    print("\nYour authors:")
    for author, count in sorted(authors.items()):
        print(f"   {author} - {count} book{'s' if count > 1 else ''}")
            

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
            update_book(library)
        elif choice == "6":
            statistic(library)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice - try again")


if __name__ == "__main__":
    main()