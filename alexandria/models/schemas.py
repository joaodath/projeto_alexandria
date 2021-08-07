from datetime import datetime
from alexandria.run import db
from sqlalchemy import exists

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    
    def __init__(self, name):
        self.name = name
       

    
    # forma bonita de mostrar o nome do registro
    def __repr__(self):
        return f'<Author {self.name}>'
    
    
    
class Publisher(db.Model):
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    
    def __init__(self, name):
        self.name = name
        
        
        
class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    year_published = db.Column(db.String(20))
    isbn = db.Column(db.String(255))
    synopsis = db.Column(db.Text)
    release_year = db.Column(db.Text)
    rating = db.Column(db.Float(2, 2)) # rever casas decimais
    genre = db.Column(db.String(100))
    pages = db.Column(db.Integer)
    image = db.Column(db.String)
    download = db.Column(db.String)
    buy = db.Column(db.String)
    published_at = db.Column(db.DateTime(), default = datetime.strftime(datetime.today(), "%b %d %Y"))
    updated_at = db.Column(db.DateTime(), default = datetime.strftime(datetime.today(), "%b %d %Y"))
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)
    
    
    author = db.relationship('Author', backref=db.backref('book',  lazy=True))
    publisher = db.relationship('Publisher', backref=db.backref('book',  lazy=True))
    
    
    def __init__(self, name, author_id, publisher_id):
        self.name = name
        self.author_id = author_id
        self.publisher_id = publisher_id
    
        
    
    def __repr__(self):
        return f'<Author {self.name}>'

