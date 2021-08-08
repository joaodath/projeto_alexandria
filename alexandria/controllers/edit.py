from flask import render_template, redirect, request

from alexandria.run import app, db
from alexandria.models.schemas import Book


@app.route('/editar-livro/<id>', methods=['POST', 'GET'])
def edit(id):
    book = Book.query.get(id)
    if request.method == 'POST':
        book.name = request.form['book']
        book.author = request.form['author']
        book.publisher = request.form['publisher']
        db.session.commit()
        return redirect('acervo')
    
    return render_template('edit.html', book=book)
