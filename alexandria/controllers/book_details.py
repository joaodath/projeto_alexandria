from flask import render_template 

from alexandria.run import app
from alexandria.models.schemas import Book



@app.route('/detalhelivro/<id>')
def book_details(id):
    book = Book.query.get(id)
    if book.image != None:
            url_img = book.image
    else:
        url_img = '../frontend/static/img/placeholder_cadastro'
    return render_template('book_details.html', book=book,url_img=url_img)
