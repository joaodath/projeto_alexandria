from flask import render_template, redirect, request

from alexandria.run import app, db

from alexandria.models.schemas import Author, Book, Publisher


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    # codigo 
    if request.method == 'POST':
        
        author = request.form['author']
        exists_author = bool(Author.query.filter_by(name=author).first())
        if exists_author == False:
            author = Author(name=author)
            db.session.add(author)
            db.session.commit()
            
        publisher = 'na mão'
        publisher_name = bool(Publisher.query.filter_by(name=publisher).first())
        if publisher_name == False:
            publisher = Publisher(name=publisher)
            db.session.add(publisher)
            db.session.commit() 
        else:
            return redirect('cadastrar')
        
        
        

        return redirect('/acervo')
    
    return render_template('cadastrar.html')

