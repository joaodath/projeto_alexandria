from flask import render_template


from alexandria.run import app
from alexandria.models.schemas import Book

@app.route('/confirmar-excluir/<id>')
def delete_confirm(id):
    """
    Router with confirme delete book

    Args:
        id ([Integer]): Register info database

    Returns:
        Templates e variables: render template with delete.html page and 
         variable book 
    """
    book = Book.query.get(id)
    return render_template('delete.html', book=book)
