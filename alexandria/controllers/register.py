from flask import render_template, redirect, request
from flask import url_for

from alexandria.run import app, db

from alexandria.models.schemas import Book


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        book = Book(
            request.form['name-book'],
            request.form['name-author']
            )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('cadastrar'))
    
    return render_template('cadastrar.html')

