from multiprocessing.dummy import active_children
from rest_framework.response import Response
from rest_framework import generics, permissions
from . models import NewUser
from locale import currency
import stripe
from . serializers import UserSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class UserView(ObjectMultipleModelAPIView):
   def get_querylist(self):
    user = self.request.query_params['user']
    querylist = (
        {'queryset': NewUser.objects.filter(username=user), 'serializer_class': UserSerializer},
    )
    return querylist




@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)