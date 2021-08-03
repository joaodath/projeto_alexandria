from flask import render_template, request

from alexandria.run import app, db




@app.route('/acervo', methods=['GET', 'POST'])
def acervo():
    
    return render_template('collections.html')



