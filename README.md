# django-practice
Practice with Django Framework for Python by creating an Inventory Web App


Django is a python web framework. It works with apache or engineX.

It allows for:
-Object Relational Mapping (ORM)
-Database Querying
-URL routing
-HTML Templating
-Form Handling
-Unit Testing

Useful Commands:
1) To start a new project-
  django-admin startproject <projectname>

2) To reference list of subcommands-
  python manage.py

3) To start a server -
  python manage.py runserver

4) To Display differences between the current settings file and the Django default settings -
  python manage.py diffsettings



Files created in Django project:
  -You may edit the following-

* settings.py (configures Django)
* urls.py (routes requests based on URL)


  -DO NOT edit the following-

* __init__.py (tells Django where the project folder is)
* manage.py (runs commands)
* wsgi.py (provides hook for webserver)


##Project vs App

App refers to python project components. Examples of components include blog, wiki, forum, etc.

###Pieces of an APP

* models.py (Data Layer)
* admin.py (Administrative Interface)
* views.py (control layer)
* tests.py (Tests the app)
* migrations (Holds migration files)

A settings file is just a python module with module-level variables.

ex:

Allowed_Hosts = ['www.example.com']
DEBUG = False
DEFAULT_FROM_EMAIL = 'webmaster@example.com'

*You can assign settings dynamically using normal python syntax


##Settings that need to be changed in settings.py

- Installed_APPS (when adding new Django app)
- TEMPLATES (when adding templates for the first time)
- STATICFILES_DIRS (adding static assets for the first time)


##Settings that may need to be changes in settings.py

- Debug (when deploying to production, set to false)
- Databases (when changing engines such as PostgreSQL, MySQL, etc.)
- Smaller settings when needed (consult documentation)
  ex: static root, admin, configurations



##Models.py

Models.py is responsible for creating a data layer of the app. Here you define the database structure. It also allows you to query the database.

A model is a class inheriting from django.db.models. It is used to define fields as class attributes for each record.


## Field Types

-Textual Data
  * CharField, TextField, EmailField, URLField

-Numeric Data
  *IntegerField, DecimalField

-File Data
  *FileField, ImageField

-Misc Data
  *BooleanField, DateTimeField

ex: models.CharField(max_length=10, null=True, blank=True)

##Field Attribute Options
  [django/docs/models/fields]

-max_length (CharField)
-null (no data)
-blank (emptry string)
-default (default value)
-choices (limit choices)

##Migrations

Migrations generates scripts to change the database structure. The initial migration creates corresponding database tables when a new model is defined. Additional migrations are needed when adding a db field, removing a field, or changing a field.

###Migration Commands
- python manage.py make migrations
- python manage



