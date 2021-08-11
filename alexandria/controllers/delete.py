from flask import redirect

from alexandria.run import app, db
from alexandria.models.schemas import Book

@app.route('/deletar/<id>')
def delete(id):
    """
    Router with confirmation of permanent deletion of the book.

    Args:
        id ([Integer]): Register info database

    Returns:
        Templates e variables: redirect route collection
    """
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/acervo')
    