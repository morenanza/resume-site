# Resume Site

Resume is a Django APP

## Installation

First of all, create a virtual env:
```bash
python -m venv env
```
And activate it: 
```bash
env\Scripts\activate.bat
```

Then, install django:
```bash
pip3 install django
```

And create a Django project
```bash
django-admin startproject my_project .
```

At this point, clone this repository in the main folder.

Open my_project/settings.py and add "resume" into INSTALLED_APPS array.

Open my_projects/urls.py and add 
```python
path('', include("resume.urls"))
```

To run website:
```python
 python manage.py runserver
```

If doesn't recognize app, before cloning this repository create django app named "resume"

```bash
python manage.py startapp resume
```

## Usage

To do migration:

```bash
#first
python manage.py makemigrations
#then
python manage.py migrate
```
