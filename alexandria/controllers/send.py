from flask import render_template,request
from flask_mail import Mail, Message
from alexandria.run import app

class Contato:
    def __init__ (self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'testesthay@gmail.com',
    "MAIL_PASSWORD": 'SENHABLUE@'
}
app.config.update(mail_settings) #atualizar as configurações do app com o dicionário mail_settings
mail = Mail(app)

@app.route('/send', methods = ['GET', 'POST'])
def send():
    if request.method == 'POST': #Capiturando as informações do formulário com o request do Flask e criando o objeto formContato
        formContato = Contato(
        request.form['nome'],
        request.form['email'],
        request.form['mensagem']
        )
        msg = Message(
        subject = 'Contato do seu Portfólio',
        sender = app.config.get("MAIL_USERNAME"),
        recipients=[app.config.get("MAIL_USERNAME")],
        body = f'''{formContato.nome} com o email {formContato.email}, te mandou a seguinte mensagem: {formContato.mensagem}''')
        mail.send(msg)
    return render_template('send.html', formContato = formContato)