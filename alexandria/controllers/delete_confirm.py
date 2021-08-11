from flask import render_template


from alexandria.run import app
from alexandria.models.schemas import Book

@app.route('/confirmar-excluir/<id>')
def delete_confirm(id):
    book = Book.query.get(id)
    return render_template('delete.html', book=book)
