from django.contrib import admin
from . models import NewUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserAdminConfig(UserAdmin):
    ordering = ('username',)
    list_display = ('username','email', 'status','is_active','is_staff')
    fieldsets = (
        (None,{'fields':('email','username','status',)}),
        ('Permissions',{'fields':('is_staff','is_active')}),
        ('Personal',{'fields':('bookmarks','history')})

    )
admin.site.register(NewUser, UserAdminConfig)