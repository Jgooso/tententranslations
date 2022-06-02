from multiprocessing.dummy import active_children
from rest_framework.response import Response
from rest_framework import generics, permissions
from . models import Novel, Chapter
from . serializers import NovelSerializer, ChapterSerializer
from . forms import NovelForm
from . scripts import download, update, upload
from django.shortcuts import render
from django.http import HttpResponse
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django.contrib.auth.forms import UserCreationForm

# RetrieveAPIView - used for read-only endpoints to represent a single model instance.
# https://www.django-rest-framework.org/api-guide/generic-views/#retrieveapiview

class MultiNovelView(ObjectMultipleModelAPIView):
   def get_querylist(self):
    tier = int(self.request.query_params['tier'])
    allchapters=Chapter.objects.filter(active__lte=tier).exclude(chapterNumber=0,active=0)
    releasechapters = Chapter.objects.filter(content='a')
    novels = Novel.objects.filter(active=True)
    for nvl in novels:
        releasechapters = releasechapters | allchapters.filter(novel=nvl).order_by("-chapterNumber")[:2]
    querylist = (
        {'queryset':novels, 'serializer_class': NovelSerializer},
        {'queryset': releasechapters, 'serializer_class': ChapterSerializer},
    )
    return querylist
class SingleNovelView(ObjectMultipleModelAPIView):
   def get_querylist(self):
    title = self.request.query_params['novel']
    tier = int(self.request.query_params['tier'])
    querylist = (
        {'queryset': Novel.objects.filter(id=title), 'serializer_class': NovelSerializer},
        {'queryset': Chapter.objects.filter(novel=title, active__lte=tier).exclude(active=0).order_by('chapterOrder'), 'serializer_class': ChapterSerializer},
    )
    return querylist
def contact(request):
    if request.method == 'POST':
        form = NovelForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            tags = form.cleaned_data['tags']
            genres = form.cleaned_data['genres']
            #download(URL=url,genres=genres,tags=tags)
            

    form = NovelForm
    novels = Novel.objects.all()
    args = {'form':form, 'novels':novels,'range': range(8,21)}
    upload()
    return render(request ,'forms.html',args)

class UpdateNovel(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Novel.objects.all()
    serializer_class=NovelSerializer
    lookup_field='id'

def uploadNovel(requests):
    print(requests)
    upload()
    return HttpResponse('hello',requests)