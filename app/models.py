from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), index=True)
    sec_name = db.Column(db.String(200), index=True)
    books = db.relationship("Book", secondary='author_book', backref=db.backref("authors", lazy='dynamic'))
    author_book = db.relationship("AuthorBook", back_populates="author")

    def __str__(self) -> str:
        return f'<Author {self.first_name} {self.sec_name}>'
    

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True, unique=True)
    genre = db.Column(db.String(100))
    description = db.Column(db.Text)
    author_book = db.relationship("AuthorBook", back_populates="book")
    
    def __str__(self) -> str:
        return f"<Book {self.name}>"
    

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_author_id = db.Column(db.Integer, db.ForeignKey('author_book.id'))
    borrower_name = db.Column(db.String(100))
    borrower_date = db.Column(db.Text)
    return_date = db.Column(db.Text)
    returned = db.Column(db.Boolean, default=False)
    author_book = db.relationship('AuthorBook', back_populates='loans')
    
class AuthorBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship("Book", back_populates="author_book")
    author = db.relationship("Author", back_populates="author_book")
    loans = db.relationship('Loan', back_populates='author_book')
