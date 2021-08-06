from flask import render_template , request

from alexandria.run import app, db




@app.route('/sobre', methods=['GET', 'POST'])
def sobre():
    # codigo 
    return render_template('quemsomos.html')