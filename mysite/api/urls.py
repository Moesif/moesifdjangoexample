from django.urls import re_path

from . import views

app_name = 'api'

urlpatterns = [
    # ex: /api/users/12345
    re_path(r'^users/(?P<user_id>\w+)', views.users, name='users'),
    # ex: /api/companies/67890
    re_path(r'^companies/(?P<company_id>\w+)', views.companies, name='companies'),

]
