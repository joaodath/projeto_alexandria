from flask import render_template, request, flash
from werkzeug.utils import redirect

from alexandria.run import app, db
from alexandria.models.schemas import Book

app.secret_key = 'seilaqualsenhausarnessabagaça'

# renderiza o 
@app.route('/editartodos')
def editartodos():
    page = request.args.get('page', 1, type=int)
    per_page = 9
    book=  Book.query.paginate(page=page, per_page=per_page)
    return render_template('edit_all.html',book=book)


# função que chama a confirmação de exclusão
@app.route('/excluir/<id>')
def editar_id(id):
    book=  Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    flash('Deletado com sucesso.')
    return redirect('/editartodos')