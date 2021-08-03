
import os
#caminho absoluto pra não ter problema no sqlite

basedir = os.path.abspath(os.path.dirname(__file__)) 


DEBUG=True

# localhost postgresql
# SQLALCHEMY_DATABASE_URI='postgresql://postgres:senha@localhost/alexandria'

# host remote elephantsql
SQLALCHEMY_DATABASE_URI='postgresql://ixvlpfdh:bS5UfVLLuuDgKDWiDZIismaW1zg23WIZ@kesavan.db.elephantsql.com/ixvlpfdh'

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