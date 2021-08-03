from flask import render_template , request

from alexandria.run import app, db




@app.route('/detalhelivro', methods=['GET', 'POST'])
def book_details():
    # codigo 
    return render_template('bookdetails.html')