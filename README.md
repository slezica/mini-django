An entire Django application contained in a single file. Can `runserver`, serve static files, `makemigrations` and `migrate`,
and be served by `gunicorn`.

```bash
(env) python app.py runserver # Django server
(env) gunicorn app # Gunicorn!
```