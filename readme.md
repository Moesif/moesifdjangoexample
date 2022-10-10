# Moesif Django Example

Django is a web application framework that many developers use to serve APIs.

[Moesif](https://www.moesif.com) is an API analytics and monitoring platform. [moesifdjango](https://github.com/Moesif/moesifdjango)
is a middleware that makes integration with Moesif easy for Django based applications.

This is an example of django application with Moesif integrated. This example is based
on the quick start [tutorials of Django](https://docs.djangoproject.com/en/1.11/intro/) and [Django rest framework](http://www.django-rest-framework.org/#quickstart).

## Key files

moesifdjango's [github readme](https://github.com/Moesif/moesifdjango) already documented
the steps for setup Moesif Django. But here is the key file where the Moesif integration is added:

- `mysite/settings.py` added Moesif middleware related settings.

## How to run this example with WSGI

1. Setup [virtual env](https://docs.python.org/3.10/library/venv.html) if needed `python -m venv ENV`. Start the virtual env by `source ENV/bin/activate`

2. Install packages:
* Django 3 LTS: `pip install -r requirements.txt`  
* Django 4: `pip install -r requirements-django4.txt`

3. Be sure to edit the `mysite/setting.py` to add your Moesif application id.

  ```python
  MOESIF_MIDDLEWARE = {
      'APPLICATION_ID': 'Your Moesif Collector Application Id',
  }
  ```
  
Your Moesif Collector Application Id can be found in the [_Moesif Portal_](https://www.moesif.com/).
After signing up for a Moesif account, your Moesif Application Id will be displayed during the onboarding steps. 

You can always find your Moesif Collector Application Id at any time by logging 
into the [_Moesif Portal_](https://www.moesif.com/), click on the bottom left user profile,
and then clicking _API Keys_.

4. Run the service:

```bash
python manage.py runserver
```

5. See `urls.py` for some urls that you can hit the server with
(e.g. `http://localhost:8000/users`), and the data
should be captured in the corresponding Moesif account of the application id.

## How to run this example with ASGI

1. Setup [virtual env](https://docs.python.org/3.10/library/venv.html) if needed `python -m venv ENV`. Start the virtual env by `source ENV/bin/activate`

2. Install packages:
* Django 3 LTS: `pip install -r requirements.txt`  
* Django 4: `pip install -r requirements-django4.txt`

Also install dependencies to related to asgi

```python
pip install --no-cache asgi uvicorn gunicorn
```

3. Be sure to edit the `mysite/setting.py` to add your Moesif application id.

  ```python
  MOESIF_MIDDLEWARE = {
      'APPLICATION_ID': 'Your Moesif Collector Application Id',
  }
  ```
  
Your Moesif Collector Application Id can be found in the [_Moesif Portal_](https://www.moesif.com/).
After signing up for a Moesif account, your Moesif Application Id will be displayed during the onboarding steps. 

You can always find your Moesif Collector Application Id at any time by logging 
into the [_Moesif Portal_](https://www.moesif.com/), click on the bottom left user profile,
and then clicking _API Keys_.

4. Run the service:

```bash
gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorker
```

5. See `urls.py` for some urls that you can hit the server with
(e.g. `http://localhost:8000/users`), and the data
should be captured in the corresponding Moesif account of the application id.


**Note** : If you get `OperationalError` with Exception Value: `no such table: auth_user`, that means the schema has not been generated in database yet.
please run the following command line to resolve  
```bash
python manage.py migrate
```

Tested Python versions: `3.10.4`  
Tested Django versions: `3.2.13 (LTS)`, `4.0.5`