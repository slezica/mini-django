An entire Django application contained in a single file. This example can:

- run `runserver` in debug with static files
- run `makemigrations` and `migrate`
- render templates
- be served by `gunicorn`

```bash
# Enter environment and install:
$ python3 -m venv env
(env) $ pip install -r requirements.txt

# Make migrations and migrate:
(env) python app.py makemigrations __main__ # __main__ needed
(env) python app.py migrate __main__ # same

(env) python app.py runserver # Django server!
(env) gunicorn app # Gunicorn!
```