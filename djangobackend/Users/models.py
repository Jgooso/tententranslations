from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_user(self, username, email, password, **other_fields):
        if not email:
            raise ValueError('You must provide an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('status','Admin')
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        return self.create_user(username,email, password, **other_fields)
    
class NewUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    bookmarks = models.TextField(null=True, blank=True)
    history=models.TextField(null=True,blank=True)
    status = models.CharField(max_length=10,default='Tier0')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def __str__ (self):
        return self.username