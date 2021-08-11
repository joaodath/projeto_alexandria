from flask import render_template, request


from alexandria.run import app
from alexandria.models.schemas import Book



@app.route('/acervo')
def acervo():
    """
    Router wiht complete book info and pagination 

    Returns:
        Template and Variables: render template with collections.html page and 
         variable book 
    """
    page = request.args.get('page', 1, type=int)
    per_page = 9
    book=  Book.query.paginate(page=page, per_page=per_page)
    return render_template('collections.html', book=book)



