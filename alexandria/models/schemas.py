
from alexandria.run import db, login_manager

from werkzeug.security import generate_password_hash, check_password_hash  
from flask_login import UserMixin



@login_manager.user_loarder
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(130), nullable=False, unique=True)


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        
    # verificando a senha digitada
    def verify_password(self, password):
        return check_password_hash(self.password, password)

    
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
    
    
    def __init__(self, name, author):
        self.name = name
        self.author = author

    
        
    
    def __repr__(self):
        return f'<Author {self.name}>'

