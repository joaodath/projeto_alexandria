from flask import render_template, redirect, request

from alexandria.run import app, db

from alexandria.models.schemas import Book


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    # codigo 
    if request.method == 'POST':
        author = Book(
            request.form['book'],
            request.form['author'],
            'na mão',
            )
        db.session.add(author)
        db.session.commit()
        return redirect('/acervo')
    
    return render_template('cadastrar.html')

