# Library Management System

A simple command-line library management system written in Python. It stores book records in a text file and allows users to add, view, search for, borrow, and return books.

## Features

- Add a new book with an ID, title, and author
- View all books
- Search for a book by ID
- Mark a book as borrowed or available
- Store book records in `LibraryManagement/library_data.txt`

## Requirements

- Python 3

## Getting Started

Clone or download this project, open a terminal in the project directory, and run:

```bash
cd LibraryManagement
python main.py
```

## Usage

When the program starts, choose one of the menu options:

```text
1. Add New Book
2. View All Books
3. Search Book
4. Borrow Book
5. Return Book
6. Exit
```

### Add a book

Select option `1`, then enter the book ID, title, and author name.

### Search for a book

Select option `3` and enter the book ID.

### Borrow or return a book

Select option `4` to borrow a book or option `5` to return it. Enter the book ID when prompted.

## Project Structure

```text
LibraryManagement/
|-- main.py              # Command-line menu and application entry point
|-- library.py           # Book management and file operations
|-- library_data.txt     # Persistent book records
README.md
```

## Data Format

Book records use pipe-separated values:

```text
ID|TITLE|AUTHOR|STATUS
B101|Python Basics|John Smith|Borrowed
```

New books are created with the `Available` status.
