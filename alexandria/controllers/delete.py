from flask import render_template, request

from alexandria.run import app, db
from alexandria.models.schemas import Book

@app.route('/deletar/<id>')
def delete(id):
    """
    Router with confirmation of permanent deletion of the book.

    Args:
        id ([Integer]): Register info database

    Returns:
        Templates e variables: render collection route with a delete alert.
    """
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    # 
    alert_show = True
    page = request.args.get('page', 1, type=int)
    per_page = 9
    book=  Book.query.paginate(page=page, per_page=per_page)
    return render_template('collections.html', book=book, show=alert_show)
    