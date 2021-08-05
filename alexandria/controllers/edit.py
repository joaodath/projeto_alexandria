from flask import render_template, redirect, request

from alexandria.run import app, db
from alexandria.models.schemas import Book


@app.route('/editar-livro/<id>', methods=['POST', 'GET'])
def edit(id):
    book = Book.query.get(id)
    if request.method == 'POST':
        book.name_book = request.form['book']
        db.session.commit()
        return redirect('/acervo')
    
    return render_template('editar-livro.html', book=book)