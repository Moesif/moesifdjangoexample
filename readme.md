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
   * Django 4.2 LTS: `pip install -r requirements-django4.txt`

3. Edit the `mysite/setting.py` to add your Moesif Application ID.

    ```python
    MOESIF_MIDDLEWARE = {
        'APPLICATION_ID': 'Your Moesif Collector Application Id',
    }
    ```
  
    After you log into [Moesif Portal](https://www.moesif.com/wrap), you can get your Moesif Application ID during the onboarding steps. You can always access the Application ID any time by following these steps from Moesif Portal after logging in:

    a. Select the account icon to bring up the settings menu.
    
    b. Select **Installation** or **API Keys**.
    
    c. Copy your Moesif Application ID from the **Collector Application ID** field.

    Also make sure you specify your time zone in [the `TIME_ZONE` setting](https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-TIME_ZONE) in `mysite/settings.py` file.

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
      pip install --no-cache uvicorn gunicorn
      ```

3. Be sure to edit the `mysite/setting.py` to add your Moesif Application ID.

    ```python
    MOESIF_MIDDLEWARE = {
        'APPLICATION_ID': 'Your Moesif Collector Application Id',
    }
    ```
  
    After you log into [Moesif Portal](https://www.moesif.com/wrap), you can get your Moesif Application ID during the onboarding steps. You can always access the Application ID any time by following these steps from Moesif Portal after logging in:

    a. Select the account icon to bring up the settings menu.
    
    b. Select **Installation** or **API Keys**.
    
    c. Copy your Moesif Application ID from the **Collector Application ID** field.

    Also make sure you specify your time zone in the `TIME_ZONE` setting in `mysite/settings.py` file.

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

## Tested Python and Django versions
Tested Python versions: `3.10.4`, `3.12.3`  
Tested Django versions: `3.2.13` LTS, `4.2.0` LTS