try:
    from django.urls import re_path as re_path_url
except ImportError:
    from django.conf.urls import url as re_path_url

from . import views

app_name = 'api'

urlpatterns = [
    # ex: /api/users/12345
    re_path_url(r'^users/(?P<user_id>\w+)', views.users, name='users'),
    # ex: /api/companies/67890
    re_path_url(r'^companies/(?P<company_id>\w+)', views.companies, name='companies'),

]
