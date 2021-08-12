from flask import render_template 

from alexandria.run import app
from alexandria.models.schemas import Book



@app.route('/detalhelivro/<id>')
def book_details(id):
    """
    Router info details book
    
    Args:
        id ([Integer]): Register info database

    Returns:
        template and Variables:  render template book details and variables 
        book[id] / url_img with info rescpective
    """
    book = Book.query.get(id)
    if book.image != None:
            url_img = book.image
    else:
        url_img = '../frontend/static/img/placeholder_cadastro'
    return render_template('book_details.html', book=book,url_img=url_img)


@app.route('/detalhelivro-editado/<id>')
def book_details_ok(id):
    """
    Router info details book
    
    Args:
        id ([Integer]): Register info database

    Returns:
        template and Variables:  render template book details and variables 
        book[id] / url_img with info rescpective
    """
    book = Book.query.get(id)
    if book.image != None:
            url_img = book.image
    else:
        url_img = '../frontend/static/img/placeholder_cadastro'
    alert_show = True
    return render_template('book_details.html', book=book,url_img=url_img, show=alert_show)