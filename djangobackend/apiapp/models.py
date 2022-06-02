from audioop import maxpp
from contextlib import nullcontext
from locale import normalize
from multiprocessing.sharedctypes import Value
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator


def upload_to(instance,filename):
    return 'novels/{filename}'.format(filename=filename)

class Novel (models.Model):
    id = models.SlugField(max_length=511, primary_key=True)
    title = models.CharField(max_length=300)
    alternativetitle = models.CharField(max_length=250)
    url = models.CharField(max_length = 34)
    author = models.CharField(max_length = 250)
    description = models.TextField()
    genres = models.TextField()
    tags = models.TextField()
    status = models.IntegerField(validators=[MaxValueValidator(2),MinValueValidator(0)])
    release = models.IntegerField()
    completed = models.IntegerField(validators=[MaxValueValidator(2),MinValueValidator(0)])
    last_updated = models.DateTimeField(null=True,blank=True)
    first_upload = models.DateTimeField(null=True,blank=True)
    image = models.ImageField(("Image"),upload_to=upload_to,blank=True,null=True)
    active=models.BooleanField()
    views=models.IntegerField()
    rating=models.DecimalField(validators=[MaxValueValidator(5.0),MinValueValidator(0.0)],max_digits=2,decimal_places=1,default=0)
    def __str__(self):
        return self.title
class Chapter(models.Model):
    id = models.SlugField(max_length=511, primary_key=True)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    title = models.CharField(max_length=511)
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    chapterNumber = models.IntegerField(null=True)
    section = models.IntegerField()
    active = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    chapterOrder = models.IntegerField()
    def __str__(self):
        return self.title
class Schedule(models.Model):
    day = models.CharField(max_length=9)
    time = models.CharField(max_length=5)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.day +" "+self.time

