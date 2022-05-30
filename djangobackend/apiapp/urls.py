from xml.dom.minidom import Document
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . views import MultiNovelView, SingleNovelView, UpdateNovel,contact

urlpatterns = [
    path('novels/',MultiNovelView.as_view(), name = 'novels_view'),
    path('singlenovel/',SingleNovelView.as_view(),name = 'single_novels_view'),
    path('',contact),
    path('novels/edit/novel/<slug:pk>',UpdateNovel.as_view(),name='editNovel')
    
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
