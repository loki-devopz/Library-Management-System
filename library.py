
"""
Library Module
Handles book records using file operations.
"""

FILE_NAME = "library_data.txt"


def initialize_file():
    """Create the library file if it does not exist."""

    try:
        with open(FILE_NAME, "x") as file:
            file.write("ID|TITLE|AUTHOR|STATUS\n")

    except FileExistsError:
        pass

    except PermissionError:
        print("Permission denied while creating the file.")


def add_book(book_id, title, author):
    """Add a new book to the library."""

    try:
        with open(FILE_NAME, "a") as file:

            file.write(
                f"{book_id}|{title}|{author}|Available\n"
            )

        print("Book added successfully!")

    except PermissionError:
        print("You do not have permission to modify the file.")

    except OSError as error:
        print("File operation failed:", error)


def view_books():
    """Read and display all library records."""

    try:
        with open(FILE_NAME, "r") as file:

            print("\n========== LIBRARY BOOKS ==========")

            for line in file:

                print(line.strip())

    except FileNotFoundError:
        print("Library file does not exist.")

    except PermissionError:
        print("You do not have permission to read this file.")


def search_book(search_id):
    """Search for a book using its ID."""

    try:
        with open(FILE_NAME, "r") as file:

            for line in file:

                details = line.strip().split("|")

                if details[0] == str(search_id):
                    print("\nBook Found!")
                    print("ID:", details[0])
                    print("Title:", details[1])
                    print("Author:", details[2])
                    print("Status:", details[3])

                    return True

        print("Book not found.")
        return False

    except FileNotFoundError:
        print("Library file does not exist.")
        return False

    except PermissionError:
        print("Permission denied.")
        return False


def update_book_status(book_id, new_status):
    """Update a book's availability status."""

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        updated = False

        for i in range(1, len(lines)):

            details = lines[i].strip().split("|")

            if details[0] == str(book_id):

                if details[3] == new_status:
                    print("Book is already", new_status)
                    return

                details[3] = new_status

                lines[i] = "|".join(details) + "\n"

                updated = True
                break

        if updated:

            # Write updated records back to file
            with open(FILE_NAME, "w") as file:
                file.writelines(lines)

            print("Book status updated successfully!")

        else:
            print("Book not found.")

    except FileNotFoundError:
        print("Library file does not exist.")

    except PermissionError:
        print("Permission denied while updating records.")

    except OSError as error:
        print("File operation failed:", error)
