import os, sys, django
from django.conf import settings

def path_to(*parts):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)


# ----------------------------------------------------------------------------------------------------------------------
# Configuration:

APP_NAME = 'app'

if not settings.configured:
    sys.modules[APP_NAME] = sys.modules[__name__] # put ourselves in the module cache under APP_NAME

    settings.configure(
        DEBUG = (__name__ == '__main__'),
        INSTALLED_APPS = [ APP_NAME ],

        ROOT_URLCONF = APP_NAME,
        ALLOWED_HOSTS = ['*'],

        MIGRATION_MODULES = { APP_NAME: 'migrations' },
        DATABASES = {
            'default': {
                # NOTE: leave an empty dict here if not using a database, this entry is still required.
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': path_to('db.sqlite3'),
            }
        },

        TEMPLATES = [
            {"BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [ path_to("templates") ]}
        ],

        STATIC_URL = "/static/",
        STATICFILES_DIRS = (path_to("static"),)
    )
    
    django.setup()


# Import only after call to `setings.configure()`:
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.db import models
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse


# ----------------------------------------------------------------------------------------------------------------------
# Models

class BaseModel(models.Model):
    class Meta:
        abstract = True
        app_label = APP_NAME

class MyModel(BaseModel):
    pass


# ----------------------------------------------------------------------------------------------------------------------
# Views

def index(request):
    MyModel().save()
    return render(request, 'index.html', { 'count': MyModel.objects.count() })


# ----------------------------------------------------------------------------------------------------------------------
# Urls

urlpatterns = [
    path("", index),
    *staticfiles_urlpatterns()
]


# ----------------------------------------------------------------------------------------------------------------------
# Main

if __name__ == "__main__":
    from django.core import management
    management.execute_from_command_line()
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

