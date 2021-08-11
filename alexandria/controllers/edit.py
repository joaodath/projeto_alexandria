from flask import render_template, redirect, request

from alexandria.run import app, db
from alexandria.models.schemas import Book


@app.route('/editar-livro/<id>', methods=['POST', 'GET'])
def edit(id):
    book = Book.query.get(id)
    url_img = ""
    if book.image != None:
        url_img = book.image
    else:
        url_img = '../frontend/static/img/placeholder_cadastro'
    if request.method == 'POST':
        book.name = request.form['name-book']
        book.author = request.form['name-author']
        book.publisher = request.form['publisher']
        db.session.add(book)
        db.session.commit()

        return redirect(f'/detalhelivro/{book.id}')
    
    return render_template('edit.html', book=book,url_img=url_img)
