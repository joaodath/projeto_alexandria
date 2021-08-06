
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__, template_folder='./frontend/templates',static_folder='./frontend/static')

# recebendo as configurações do banco de dados
app.config.from_object('config')

# cabeçalho de cache 
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

# db recebe a instância de SQLAlchemy com parametro app
db = SQLAlchemy(app)

# instancia que vai controlar as migrações do banco de dados
migrate = Migrate(compare_type=True)
migrate.init_app(app, db) # recebe a app e o banco

# controle de informação
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# importando as models/schemas
from alexandria.models import schemas

# importando os controllers/páginas/rotas
from .controllers import home
from .controllers import about
from .controllers import book_details
from .controllers import collection
from .controllers import edit
from .controllers import register
from .controllers import delete

#Cache Control
# @app.after_request
# def add_security_headers(resp):
#     resp.headers['Content-Security-Policy']='default-src \'self\''
#     return resp

