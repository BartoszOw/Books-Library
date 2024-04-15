# Books Library

## Description:

The Books Library project is designed to manage a library's book inventory and loan system. The project utilizes a SQLite database (library.db) to store information about books, authors, loans, and their relationships.

## Features:

1. Data Model:

- `Author:` Represents an author of a book. Each author can have multiple books attributed to them.
- `Book:` Represents a book in the library, including details such as name, genre, description, and its relationship with authors.
- `Loan:` Tracks the loans made by borrowers, including the borrower's name, loan date, return date, and whether the book has been returned.
- `AuthorBook:` A many-to-many relationship table linking authors and books, allowing multiple authors to be associated with multiple books.
2. Web Interface:

- The project provides a web interface built using Flask, HTML, CSS (Bootstrap), and Jinja templating.
- The homepage displays a list of books available in the library along with information on books that have been loaned out.
- Users can view details of each book, including its authors and loan status.
- The interface allows for easy navigation and interaction with the library's inventory.
## Files:

- `app/models.py:` Defines SQLAlchemy models for Author, Book, Loan, and AuthorBook, representing the data structure of the library.
- `app/init.py:` Initializes the Flask application, configures the database, and sets up SQLAlchemy and Flask-Migrate.
- `config.py:` Contains configuration settings for the Flask application, including the database URI and secret key.
- `library.py:` Defines routes and functions for the web interface, including the homepage route to render the library's inventory.
## Usage:

- Clone the repository to your local machine.
  ```
  git clone https://github.com/BartoszOw/Books-Library.git
  ```
- Set up a virtual environment and install the required dependencies `(Flask, Flask-SQLAlchemy, Flask-Migrate, Jinja2, Bootstrap)`.
- Run the Flask application using `flask run` command.
- Access the web interface through a web browser.
Contributing:

Contributions to the project are welcome. Feel free to submit bug reports, feature requests, or pull requests through GitHub.

## Acknowledgments:

This project was inspired by the need for a simple yet effective solution to manage a library's book inventory and loan system.

## License:

This project is licensed under the MIT License - see the LICENSE file for details.
