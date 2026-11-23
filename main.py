
"""
Library Management System
Main Application
"""

from library import (
    initialize_file,
    add_book,
    view_books,
    search_book,
    update_book_status
)


def display_menu():
    """Display the library management menu."""

    print("\n" + "=" * 40)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add New Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")


def add_new_book():
    """Get book details from the user."""

    book_id = input("Enter Book ID: ").strip()

    title = input("Enter Book Title: ").strip()

    author = input("Enter Author Name: ").strip()

    if not book_id or not title or not author:
        print("All fields are required.")
        return

    add_book(book_id, title, author)


def borrow_book():
    """Mark a book as borrowed."""

    book_id = input("Enter Book ID to borrow: ").strip()

    update_book_status(book_id, "Borrowed")


def return_book():
    """Mark a borrowed book as available."""

    book_id = input("Enter Book ID to return: ").strip()

    update_book_status(book_id, "Available")


# Initialize storage file
initialize_file()


# Main application loop
while True:

    display_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":

        add_new_book()

    elif choice == "2":

        view_books()

    elif choice == "3":

        book_id = input("Enter Book ID to search: ").strip()

        search_book(book_id)

    elif choice == "4":

        borrow_book()

    elif choice == "5":

        return_book()

    elif choice == "6":

        print("Thank you for using the Library System!")
        break

    else:

        print("Invalid choice. Please try again.")
