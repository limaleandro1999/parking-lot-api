# Parking Lot API

## Used Tools

- Python
- Django
- Django Rest Framework
- Django Admin
- DRF yasg

## How to start

You should install `pipenv` to manage your project environment:

```sh
$ pip install -U pip
$ pip install pipenv
$ pipenv sync --dev
```

Enable virtualenv with pipenv:

```sh
$ pipenv shell
```

Apply migrations into database:

```sh
$ python manage.py migrate
```

Create a new user to access the admin site:

```sh
$ python manage.py createsuperuser
```

And then, start the server:

```sh
$ python manage.py runserver
```

Now you can check it out on http://127.0.0.1:8000/api/

## API endpoints

You can see all the API endpoints on http://127.0.0.1:8000/docs/
