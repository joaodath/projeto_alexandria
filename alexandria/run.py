
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__, template_folder='./frontend/templates',static_folder='./frontend/static')

# recebendo as configurações do banco de dados
app.config.from_object('config')

# db recebe a instância de SQLAlchemy com parametro app
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# instancia que vai controlar as migrações do banco de dados
migrate = Migrate(compare_type=True)
migrate.init_app(app, db, login_manager) # recebe a app e o banco

# controle de informação
manager = Manager(app,login_manager)
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
from .controllers import login
from .controllers import signup

