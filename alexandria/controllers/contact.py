from flask import render_template , request

from alexandria.run import app, db




@app.route('/contato')
def contact():
    # codigo 
    return render_template('contact.html')