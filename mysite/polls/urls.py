try:
    from django.urls import re_path as re_path_url
except ImportError:
    from django.conf.urls import url as re_path_url

from . import views

app_name = 'polls'

urlpatterns = [
    re_path_url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    re_path_url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    re_path_url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    re_path_url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
