from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
    # ex: /api/users/12345
    url(r'^users/(?P<user_id>\w+)', views.users, name='users'),
    # ex: /api/companies/67890
    url(r'^companies/(?P<company_id>\w+)', views.companies, name='companies'),

]
