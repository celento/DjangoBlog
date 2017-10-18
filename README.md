# Blogging platform in Python using Django
### A blogging app written in Python using the Django web framework

This project requires you to install the following components. 
* Python 3.x
* Django

Note: If you are using Python 2.x, a few lines of code needs to be modified.
If the app needs to be included in an existing project, include 'blogapp' inside the installed apps (settings.py).

New posts can be added using the admin panel included with every Django installation.

### Few common commands

##### Start server
`python manage.py runserver`

##### Mirgrate
`python manage.py makemigrations`
`python manage.py sqlmigrate`

`django-admin migrate [app_label] [migration_name]`

For more, see the [official Django documentaion](https://docs.djangoproject.com/en/1.11/)

Includes a copy of Bootstrap v3.3.7. Uses SQLITE database.

###### If you are planning to run the entire project, the login credentials for the admin panel is as follows:
`>username : admin`
`>password : password! (password followed by an exclamation mark !)`

-------
Life is short. Use Python.
