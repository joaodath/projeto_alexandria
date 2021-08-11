
import os
#caminho absoluto pra não ter problema no sqlite

basedir = os.path.abspath(os.path.dirname(__file__)) 


DEBUG=True

# localhost postgresql
# SQLALCHEMY_DATABASE_URI='postgresql://postgres:senha@localhost/alexandria'

# host remote elephantsql
SQLALCHEMY_DATABASE_URI='postgresql://yplcqsod:7zYLgQpctwTio0jipae_zPbJXb5x4lFg@kesavan.db.elephantsql.com/yplcqsod'

# notificações SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS=True

# Localhost SQLite3 
# SQLALCHEMY_DATABASE_URI= 'sqlite:///' + os.path.join(basedir, 'alexandria.db')


# Início
# Acervo
# Cadastrar
# Quem Somos
# Página do Livro
# Editar

# fru-fru
# Login
# Cadastrar