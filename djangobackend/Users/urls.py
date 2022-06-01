from xml.dom.minidom import Document
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . views import UserView,stripe_config

urlpatterns = [
    path('user/',UserView.as_view(),name = 'user_view'),
    path('config/', stripe_config)
    
   
]
