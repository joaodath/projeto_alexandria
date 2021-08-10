
from flask import render_template

from alexandria.run import app, db
from alexandria.cache_control import cache



@app.route('/')
# @cache(None)
def index(): 
    return render_template('index.html')




