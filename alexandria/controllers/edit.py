from flask import render_template

from alexandria.run import app, db




@app.route('/editar')
def index(): 
    return render_template('edit.html')
