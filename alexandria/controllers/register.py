from flask import render_template, request
from kan_alexandria.book_api import search_book_kan as search


from alexandria.run import app, db
from alexandria.models.schemas import Book


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    """
    Route register book information in the database with alexandria api.
    
    Returns:
        Templates and Variables: render template register.html and variable
        book
    """
    if request.method == 'POST':
        book_dict = search(request.form['name-book'],
            request.form['name-author'])
        
        #Validating the book      
        for k, v in book_dict.items():
            if book_dict[k] == ' ':
                book_dict[k] = 'N/A'
        if book_dict['title'] == None or book_dict['title'] == 'N/A':
            book_dict['title'] = request.form['name-book']
        if book_dict['author'] == None or book_dict['author'] == 'N/A':
            book_dict['author'] = request.form['name-author']
        if book_dict['pageCount'] == None or book_dict['pageCount'] == 'N/A':
            book_dict['pageCount'] = 0
        if book_dict['img'] == None or book_dict['img'] == 'N/A':
            book_dict['img'] = '/static/img/placeholder_biblioteca.png'
            

        #Uploading the book to the database
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

