#!venv/bin/python
import os
from app import app
port = int(os.environ.get('PORT', 33507))
app.run(host='0.0.0.0', port=port, debug=False)

#web: gunicorn run:app
