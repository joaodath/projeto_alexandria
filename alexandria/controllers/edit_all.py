from flask import render_template, redirect, request

from alexandria.run import app, db
from alexandria.models.schemas import Book


@app.route('/editartodos')
def editartudo():
    return render_template('edit_all.html')