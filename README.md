# Blogicum

A Django blogging application with categories, locations, scheduled publications and an admin interface.

## Features

- Blog posts with author, category, location and publication date
- Scheduled posts: content is shown only after the publication time
- Publication status for posts and categories
- Category pages and individual post pages
- Optimized ORM queries with `select_related`
- Django admin configuration for posts, categories and locations
- Automated tests with `pytest`
- Code style checks with `flake8`

## Tech stack

- Python
- Django 5.1
- Django ORM
- HTML / Django Templates
- SQLite
- pytest / pytest-django
- flake8

## Project structure

```text
blogicum/
├── blog/          # models, views, urls and admin
├── blogicum/      # project settings
├── pages/         # static pages
├── static/        # static files
├── templates/     # HTML templates
└── manage.py
```

## Run locally

```bash
git clone https://github.com/samedovv1/django-sprint3.git
cd django-sprint3

python -m venv venv
```

Activate the virtual environment:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Install dependencies and start the project:

```bash
pip install -r requirements.txt
cd blogicum
python manage.py migrate
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Tests

From the repository root:

```bash
pytest
```

## What this project demonstrates

This project demonstrates practical Django backend skills: designing relational models, working with the ORM, filtering querysets, building views and URL routes, configuring the admin panel, templates, migrations and automated tests.
