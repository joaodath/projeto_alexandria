from flask import render_template

from alexandria.run import app
from alexandria.models.schemas import Author, Book



@app.route('/acervo')
def acervo():
    author = Author.query.all()
    book = Book.query.all()
    return render_template('acervo.html', author=author, book=book)



