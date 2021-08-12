from flask import render_template, redirect, request, url_for, session
from alexandria.run import app, db


from alexandria.models.schemas import User


@app.route('/novo-usuario', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
     
        user = User(name, email, password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    
    return render_template('signup.html')

