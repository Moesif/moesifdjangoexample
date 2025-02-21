from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views import View
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GovView(View):
    def get(self, request):
        # Your logic to generate JSON data
        data = {'success': True}

        # Return JsonResponse with the data
        return JsonResponse(data)
