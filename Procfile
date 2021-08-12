web: gunicorn -k uvicorn.workers.UvicornWorker app:manager --workers 3
worker: python -u app.py runserver