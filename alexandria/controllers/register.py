from flask import render_template, request
from kan_alexandria.book_api import search_book_kan as search


from alexandria.run import app, db

from alexandria.models.schemas import Book


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        book_dict = search(request.form['name-book'],
            request.form['name-author'])
        
        book_user = Book(
                book_dict['title'],
                book_dict['author'],
                book_dict['publisher'],
                book_dict['publishedDate'],
                book_dict['isbn'],
                book_dict['description'],
                book_dict['publishedDate'],
                book_dict['categories'],
                book_dict['pageCount'],
                book_dict['img']
            )
        db.session.add(book_user)
        db.session.commit()
        
        return render_template('register.html', book=book_user)
       
    
    return render_template('register.html')

