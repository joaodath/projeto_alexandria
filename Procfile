web: gunicorn -k uvicorn.workers.UvicornH11Worker app:manager --workers 3
worker: python -u app.py runserver