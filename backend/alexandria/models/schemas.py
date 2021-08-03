from datetime import datetime
from alexandria.run import db


class Author(db.Model):
    __tablename__ = 'authors'

    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
   
    
    # relacionamento na busca
    book = db.relationship('Book', back_populates='author')
    
    def __init__(self, name):
        self.name = name
        
        
    
    # forma bonita de mostrar o nome do registro
    def __repr__(self):
        return f'<Author {self.name}>'
    

class Book(db.Model):
    __tablename__ = 'books'
    
    id_book = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_book = db.Column(db.String(255), nullable=False)
    year_published = db.Column(db.String(20))
    isbn = db.Column(db.String(255))
    synopsis = db.Column(db.Text)
    release = db.Column(db.Text)
    rating = db.Column(db.Float(10, 2))
    genre = db.Column(db.String(100))
    pages = db.Column(db.Integer)
    image = db.Column(db.String)
    download = db.Column(db.String)
    buy = db.Column(db.String)
    published_at = db.Column(db.DateTime(), nullable=True, default = datetime.strftime(datetime.today(), "%b %d %Y"))
    uptaded_at = db.Column(db.DateTime(), nullable=True, default = datetime.strftime(datetime.today(), "%b %d %Y"))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    
    # relacionamento na busca
    author = db.relationship('Author', back_populates='book')

    
    
    def __init__(self, name_book, year_published, synopsis,release, rating, genre, pages, image, download, buy):
        self.name_book = name_book
        self.year_published = year_published
        self.image = image
        self.synopsis = synopsis
        self.release = release
        self.rating = rating
        self.genre = genre
        self.pages = pages
        self.image = image
        self.download = download
        self.buy = buy
    
        
    
    def __repr__(self):
        return f'<Author {self.name_book}>'

class controller(db.Model):
    __tablename__ = 'controllers'
    id_controller = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_isbn = db.Column(db.Integer, db.ForeignKey('books.isbn'))
    id_author = db.Column(db.Integer, db.ForeignKey('authors.id'))
    
    
    def __init__(self, id_isbn, id_author):
        self.id_isbn = id_isbn
        self.id_author = id_author
        
    def __repr__(self):
        return f'<ISBN {self.id_isbn}>'