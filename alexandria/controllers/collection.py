from flask import render_template, request


from alexandria.run import app
from alexandria.models.schemas import Book



@app.route('/acervo')
def acervo():
    """[summary]

    Returns:
        [type]: [description]
    """
    page = request.args.get('page', 1, type=int)
    per_page = 3
    book=  Book.query.paginate(page=page, per_page=per_page)
    return render_template('acervo.html', book=book)



