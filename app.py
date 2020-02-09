import os, sys, django
from django.conf import settings

APP_NAME = 'app'

def path_to(*parts):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)


# Configuration:
if not settings.configured:
    sys.modules[APP_NAME] = sys.modules[__name__] # put ourselves in the module cache under APP_NAME

    settings.configure(
        DEBUG = (__name__ == '__main__'),
        ROOT_URLCONF = APP_NAME,
        
        DATABASES = {
            # NOTE: leave an empty dict in default if not using a database, this entry is still required.
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': path_to('db.sqlite3'),
            }
        },

        INSTALLED_APPS = [ APP_NAME ],

        TEMPLATES = [
            {"BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [ path_to("templates") ]}
        ],

        STATIC_URL = "/static/",
        STATICFILES_DIRS = (path_to("static"),),
        MIGRATION_MODULES = { APP_NAME: 'migrations' },

        ALLOWED_HOSTS = ['*']
    )
    
    django.setup()


# Import only after call to `setings.configure()`:
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.db import models
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse


# Models
class BaseModel(models.Model):
    class Meta:
        abstract = True
        app_label = APP_NAME

class MyModel(BaseModel):
    pass


# Views
def index(request):
    MyModel().save()
    return render(request, 'index.html', { 'count': MyModel.objects.count() })


# Urls
urlpatterns = [
    path("", index),
    *staticfiles_urlpatterns()
]


if __name__ == "__main__":
    from django.core import management
    management.execute_from_command_line()
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

