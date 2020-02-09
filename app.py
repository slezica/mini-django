import os, sys, django
from django.conf import settings


def path_to(*parts):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)

# Configuration:
if not settings.configured:
    settings.configure(
        DEBUG = (__name__ == '__main__'),
        ROOT_URLCONF = __name__,
        
        DATABASES = {
            # NOTE: leave an empty dict in default if not using a database, this entry is still required.
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'db.sqlite3',
            }
        },

        INSTALLED_APPS = [ __name__ ],

        TEMPLATES = [
            {"BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": path_to(".")}
        ],

        STATIC_URL = "/static/",
        STATICFILES_DIRS = (path_to("static"),),
        MIGRATION_MODULES = { __name__: 'migrations' },

        ALLOWED_HOSTS = ['*']
    )
    
    django.setup()


# Import only after call to `setings.configure()`:
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.db import models
from django.urls import path
from django.http import HttpResponse


# Models
class BaseModel(models.Model):
    class Meta:
        abstract = True
        app_label = __name__

class MyModel(BaseModel):
    pass


# Views
def index(request):
    MyModel().save()
    return HttpResponse("Hello! We have %d objects saved. Also, try /static/data.txt" % MyModel.objects.count())


# Urls
urlpatterns = [
    path("", index),
    *staticfiles_urlpatterns()
]


if __name__ == "__main__":
    from django.core import management
    management.execute_from_command_line()
