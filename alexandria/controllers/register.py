from flask import render_template, redirect, request
from flask.helpers import url_for

from alexandria.run import app, db

from alexandria.models.schemas import Author, Book


@app.route('/registrarlivro', methods=['GET', 'POST'])
def register():
    # codigo 
    if request.method == 'POST':
        author = Author(
            request.form['author']
            ) 
        print(author)
        db.session.add(author)
        db.session.commit() 
        
    if request.method == 'POST':
        book = Book(
            request.form['book']
            )
        db.session.add(book) 
        db.session.commit()
        return redirect(url_for('acervo'))
    
    return render_template('register.html')


    