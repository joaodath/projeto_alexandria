
from flask import render_template

from alexandria.run import app




@app.route('/')
def index(): 
    return render_template('index.html')



