from flask import render_template , request

from alexandria.run import app, db




@app.route('/sobre', methods=['GET', 'POST'])
def about():
    # codigo 
    return render_template('about.html')