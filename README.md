An entire Django application contained in the `app.py` file.

This example can:

- run `runserver` in debug with static files
- run `makemigrations` and `migrate`
- render templates
- be served by `gunicorn`

```bash
# Enter environment and install:
$ python3 -m venv env
(env) $ pip install -r requirements.txt

# Make migrations and migrate:
(env) python app.py makemigrations
(env) python app.py migrate

(env) python app.py runserver # Django server!
(env) gunicorn app # Gunicorn!
```