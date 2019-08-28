# Moesif Django Example

Django is a web application framework that many developers to serve APIs.

[Moesif](https://www.moesif.com) is an API analyatics and monitorin platform. [moesifdjango](https://github.com/Moesif/moesifdjango)
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

5. Be sure to edit the `mysite/setting.py` to add your Moesif application id.

  ```python
  MOESIF_MIDDLEWARE = {
      'APPLICATION_ID': 'your application id from moesif',
  }
  ```
  
Your Moesif Application Id can be found in the [_Moesif Portal_](https://www.moesif.com/).
After signing up for a Moesif account, your Moesif Application Id will be displayed during the onboarding steps. 

You can always find your Moesif Application Id at any time by logging 
into the [_Moesif Portal_](https://www.moesif.com/), click on the top right menu,
and then clicking _Installation_.

6. Run the service:

```bash
python manage.py runserver
```

7. See `urls.py` for some urls that you can hit the server with
(e.g. `http://localhost:8000/users`), and the data
should be captured in the corresponding Moesif account of the application id.

## Using Celery (Optional)

If you are already using Celery in your Django application to manage task queueing,
the `moesifdjango` SDK can also take advantage of the benefits. Do the following steps:

1. Install Redis by, `pip install -U "celery[redis]"`

*Please Note:* If you're using Celery 3.1 or earlier, install celery and redis with `pip install celery==3.1.25` and `pip install redis==2.10.6`

2. If you plan to use celery as the backend of asynchronous delivered logged requests,
you also need to add `moesifdjango` to your `INSTALLED_APPS`

3. Be sure to set the `USE_CELERY` to `True`

  ```python
  MOESIF_MIDDLEWARE = {
      'USE_CELERY': True
  }
  ```
