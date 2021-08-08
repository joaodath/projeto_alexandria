from flask import render_template, redirect, request, url_for
from alexandria.run import app, db
from flask_login import login_user, logout_user

from alexandria.models.schemas import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        user = User.objects.filter(email=email).first()
        
        if not user or not user.verify_password(password):
            return redirect(url_for('/'))
        
        login_user(user)
        return redirect(url_for('signup'))
    return render_template('login.html')