from flask import render_template , request

from alexandria.run import app, db
from alexandria.models.schemas import Book



@app.route('/detalhelivro/<id>')
def book_details(id):
    book = Book.query.get(id)
    return render_template('book_details.html',book=book)
