# Django — Learning Notes

This is a personal learning repo where I'm practicing Django fundamentals by building a small multi-page project from scratch.

> **Note:** This is a private repository. Access is restricted to invited collaborators.

## What I Learned / Practiced

- **Project vs. App structure** — how a Django *project* (`firstproject`) can contain multiple *apps* (`first`), each registered in `INSTALLED_APPS`
- **URL routing**
  - Mapping URLs to views with `path()` in a project-level `urls.py`
  - Using `include()` to delegate a URL prefix (`/first/`) to an app's own `urls.py`, keeping routing modular
- **Views**
  - Function-based views (`views.py`)
  - Returning a plain `HttpResponse` vs. rendering a full template with `render()`
- **Templates**
  - Setting up a project-level `template/` directory via `TEMPLATES['DIRS']` in `settings.py`
  - App-level templates using Django's `APP_DIRS` auto-discovery (`first/templates/first/...`)
  - Using `{% load static %}` and `{% static %}` to link CSS from templates
- **Static files**
  - Configuring `STATIC_URL` and `STATICFILES_DIRS` to serve custom CSS
- **Settings.py fundamentals**
  - `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` and what they're for
  - `DATABASES` config for SQLite (the default dev database)
  - `MIDDLEWARE` stack and what each default middleware does
  - `AUTH_PASSWORD_VALIDATORS`
- **Admin panel** — enabling `/admin/` and how `admin.py` is used to register models (not used yet, but scaffolded)
- **Models** — where and how Django models are defined (`models.py`), even though this app doesn't use the DB yet
- **manage.py commands** — `runserver`, `migrate`, `createsuperuser`
- **WSGI/ASGI entry points** — what `wsgi.py` and `asgi.py` are for and when each is used

## Things I Want to Learn Next

- Actually defining and migrating a model (currently `first/models.py` is empty)
- Django forms and form validation
- Class-based views vs. function-based views
- Django's ORM — querysets, filtering, relationships
- Template inheritance (`{% extends %}` / `{% block %}`) instead of repeating full HTML in every page
- Environment variables for `SECRET_KEY` / config instead of hardcoding
- Deploying a Django app properly (`DEBUG=False`, `ALLOWED_HOSTS`, static file collection)

## Running It Locally

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install django
cd firstproject
python manage.py migrate
python manage.py runserver
```