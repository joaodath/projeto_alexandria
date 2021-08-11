from flask import render_template 

from alexandria.run import app
from alexandria.models.schemas import Book



@app.route('/detalhelivro/<id>')
def book_details(id):
    book = Book.query.get(id)
    return render_template('book_details.html', book=book)
