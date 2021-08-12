from alexandria.run import db

    
class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    publisher = db.Column(db.String(255))
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
    
    
    def __init__(self, name, author, publisher, year_published, isbn, synopsis, release_year, genre, pages, image):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year_published = year_published
        self.isbn = isbn
        self.synopsis = synopsis
        self.release_year = release_year
        self.genre = genre
        self.pages = pages
        self.image = image

    
        
    def __repr__(self):
        return f'<Author {self.name}>'

