from datetime import datetime
from alexandria.run import db


class Author(db.Model):
    __tablename__ = 'authors'

    
    id_author = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_author = db.Column(db.String(255), nullable=False)
   
    
    # relacionamento na busca
    book = db.relationship('Book', back_populates='author')
    
    def __init__(self, name_author):
        self.name_author = name_author
        
        
    
    # forma bonita de mostrar o nome do registro
    def __repr__(self):
        return f'<Author {self.name_author}>'
    

class Book(db.Model):
    __tablename__ = 'books'
    
    id_book = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_book = db.Column(db.String(255), nullable=False)
    year_published = db.Column(db.String(20))
    isbn = db.Column(db.String(255))
    synopsis = db.Column(db.Text)
    release_year = db.Column(db.Text)
    rating = db.Column(db.Float(10, 2))
    genre = db.Column(db.String(100))
    pages = db.Column(db.Integer)
    image = db.Column(db.String)
    download = db.Column(db.String)
    buy = db.Column(db.String)
    published_at = db.Column(db.DateTime(), default = datetime.strftime(datetime.today(), "%b %d %Y"))
    updated_at = db.Column(db.DateTime(), default = datetime.strftime(datetime.today(), "%b %d %Y"))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id_author'))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id_publisher'))
    
    # relacionamento na busca
    author = db.relationship('Author', back_populates='book')

    
    
    def __init__(self, name_book):
        self.name_book = name_book
    
        
    
    def __repr__(self):
        return f'<Author {self.name_book}>'

class Publisher(db.Model):
    __tablename__ = 'publishers'

    id_publisher = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_publisher = db.Column(db.String(100), nullable=False)

    def __init__(self, name_publisher):
        self.name_author = name_publisher