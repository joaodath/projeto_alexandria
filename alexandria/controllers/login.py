from flask import Flask, render_template, redirect, request, url_for, session, flash
from alexandria.run import app
from flask_login import login_user
from alexandria.models.schemas import User

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
        session['email'] = None
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user = User.objects.filter(email=email).first()
            
            if not user or not user.verify_password(password):
                return redirect(url_for('/'))
            
            login_user(user)
            flash('Login feito com sucesso!')
            return redirect(url_for('/acervo'))
    
        flash('Erro no login, tente novamente!')
        return render_template('login.html')


