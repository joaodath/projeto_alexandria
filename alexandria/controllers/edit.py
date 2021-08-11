from flask import render_template, request

from alexandria.run import app, db
from alexandria.models.schemas import Book


@app.route('/editar-livro/<id>', methods=['POST', 'GET'])
def edit(id):
    book = Book.query.get(id)
    if request.method == 'POST':
        book.name = request.form['name-book']
        book.author = request.form['name-author']
        book.publisher = request.form['publisher']
        book.isbn = request.form['isbn']
        book.synopsis = request.form['synopsis']
        book.release_year = request.form['release']
        book.synopsis = request.form['synopsis']
        book.genre = request.form['genre']
        book.pages = request.form['pages']
        book.image= request.form['image']
        db.session.add(book)
        db.session.commit()
        alert_show = True
        return render_template('book_details.html', book=book, show=alert_show)
    
    return render_template('edit.html', book=book)
