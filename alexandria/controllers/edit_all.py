from flask import render_template, redirect, request

from alexandria.run import app, db
from alexandria.models.schemas import Book


@app.route('/editartodos')
def editartudo():
    page = request.args.get('page', 1, type=int)
    per_page = 9
    book=  Book.query.paginate(page=page, per_page=per_page)
    return render_template('edit_all.html',book=book)