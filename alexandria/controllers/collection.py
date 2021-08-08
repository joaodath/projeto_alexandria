from flask import render_template

from alexandria.run import app
from alexandria.models.schemas import Book



@app.route('/acervo')
def acervo():
    book = Book.query.all()
    return render_template('collections.html', book=book)


