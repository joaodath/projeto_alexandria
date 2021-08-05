from flask import render_template, request

from alexandria.run import app, db
from alexandria.models.schemas import Author, Book



@app.route('/acervo', methods=['GET', 'POST'])
def acervo():
    author = Author.query.filter_all()
    book = Book.query.filter_all()
    return render_template('collections.html', author=author, book=book)



