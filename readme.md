# Moesif Django Example

Django is a web application framework that many developers to serve APIs.

[Moesif](https://www.moesif.com) is an API analytics and monitoring platform. [moesifdjango](https://github.com/Moesif/moesifdjango)
is a middleware that makes integration with Moesif easy for Django based applications.

This is an example of django application with Moesif integrated. This example is based
on the quick start [tutorials of Django](https://docs.djangoproject.com/en/1.11/intro/) and [Django rest framework](http://www.django-rest-framework.org/#quickstart).

## Key files

moesifdjango's [github readme](https://github.com/Moesif/moesifdjango) already documented
the steps for setup Moesif Django. But here is the key file where the Moesif integration is added:

- `mysite/settings.py` added Moesif middleware related settings.

## How to run this example.

1. Setup [virtual env](https://virtualenv.pypa.io/en/stable/) if needed `virtualenv ENV`. Start the virtual env by `source ENV/bin/activate`

2. Install packages. `pip install -r requirements.txt`

5. Be sure to edit the `mysite/setting.py` to add your Moesif application id.

  ```python
  MOESIF_MIDDLEWARE = {
      'APPLICATION_ID': 'Your Moesif Application Id',
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
