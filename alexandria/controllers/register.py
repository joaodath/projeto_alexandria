from flask import render_template, redirect, request
from flask.helpers import url_for

from alexandria.run import app, db

from alexandria.models.schemas import Author, Book


@app.route('/registrarlivro', methods=['GET', 'POST'])
def register():
    # codigo 
    if request.method == 'POST':
        author = Author(
            name = request.form['name-author'],
        ) 
        db.session.add(author)
        db.session.commit() 
        
    if request.method == 'POST':
        book = Book(
            request.form['name-book'],
            request.form['year-published'],
            request.form['synopsis'],
            request.form['release'],
            request.form['rating'],
            request.form['genre'],
            request.form['pages'],
            request.form['image'],
            request.form['download'],
            request.form['buy'],
        )
        db.session.add(book) 
        db.session.commit()
        return redirect(url_for('acervo'))
    
    return render_template('register.html')


    