from flask import render_template, redirect, request
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
        return redirect('/acervo')
    
    return render_template('register.html')


    