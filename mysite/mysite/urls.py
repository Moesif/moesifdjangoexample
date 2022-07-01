"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import re_path, include
    2. Add a URL to urlpatterns:  re_path(r'^blog/', include('blog.urls'))
"""
try:
    from django.urls import include, re_path as re_path_url
except ImportError:
    from django.conf.urls import include, url as re_path_url
from django.contrib import admin
from rest_framework import routers
from apisection import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    re_path_url(r'^polls/', include('polls.urls')),
    re_path_url(r'^api/', include('api.urls')),
    re_path_url(r'^admin/', admin.site.urls),
    re_path_url(r'^', include(router.urls)),
    re_path_url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
