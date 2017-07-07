# Moesif Django Example

Django is a web application framework that many developers to serve APIs.

[Moesif](https://www.moesif.com) is an API analyatics platform. [moesifdjango](https://github.com/Moesif/moesifdjango)
is a middleware that makes integration with Moesif easy for Django based applications.

This is an example of django application with Moesif integrated. This example is based
on the quick start [tutorials of Django](https://docs.djangoproject.com/en/1.11/intro/) and [Django rest framework](http://www.django-rest-framework.org/#quickstart).

## Key files

moesifdjango's [github readme](https://github.com/Moesif/moesifdjango) already documented
the steps for setup Moesif Django. But here is the key file where the Moesif integration is added:

- `mysite/settings.py` added Moesif middleware related settings.

## How to run this example.

1. Setup [virtual env](https://virtualenv.pypa.io/en/stable/) if needed `virtualenv ENV`. Start the virtual env by `source ENV/bin/activate`

2. Install django if you haven't done so. `pip install Django`

3. Install moesifdjango in the environment by `pip install moesifdjango`

4. Install Django Rest Framework by, `pip install djangorestframework`

5. Be sure to edit the `mysite/setting.py` to change the application id to your
application id obtained from Moesif.

```
MOESIF_MIDDLEWARE = {
    'APPLICATION_ID': 'your application id from moesif',
}
```

6. `python manage.py runserver`

7. See `urls.py` for some urls that you can hit the server with
(e.g. `http://localhost:8000/users`), and the data
should be captured in the corresponding Moesif account of the application id.
