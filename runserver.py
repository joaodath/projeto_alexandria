from alexandria import app
from alexandria import run

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT'))
    app.run(host='0.0.0.0', port=port)