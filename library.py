from app import app,db
from app.models import Book, Author, AuthorBook, Loan
from flask import render_template


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Book': Book,
        'Author': Author,
        'AuthorBook': AuthorBook,
        'Loan': Loan,
    }



@app.route('/')
def homepage():

    author_book = AuthorBook.query.all()
    loans = Loan.query.all()
    return render_template('home.html', author_book=author_book, loans=loans)