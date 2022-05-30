from multiprocessing.dummy import active_children
from rest_framework.response import Response
from rest_framework import generics, permissions
from . models import NewUser
from . serializers import UserSerializer
from django.shortcuts import render
from django.http import HttpResponse
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class UserView(ObjectMultipleModelAPIView):
   def get_querylist(self):
    user = self.request.query_params['user']
    querylist = (
        {'queryset': NewUser.objects.filter(username=user), 'serializer_class': UserSerializer},
    )
    return querylist