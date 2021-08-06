from flask import redirect

from alexandria.run import app, db
from alexandria.models.schemas import Book

@app.route('/deletar/<id>')
def delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/acervo')
    