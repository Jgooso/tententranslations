from django.contrib import admin
from . models import Novel, Chapter, Schedule
from django.contrib.auth.admin import UserAdmin

admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(Schedule)






