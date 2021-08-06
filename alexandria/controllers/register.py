from flask import render_template, redirect, request


from alexandria.run import app, db

from alexandria.models.schemas import Author, Book


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
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
        return redirect('/acervo')
    
    return render_template('cadastrar.html')


    