from xml.dom.minidom import Document
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . views import UserView

urlpatterns = [
    path('user/',UserView.as_view(),name = 'user_view'),
    
   
]
