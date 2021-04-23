from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username


class medicine(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    author = models.CharField(max_length=128)
    publish_date = models.DateField()
    category = models.CharField(max_length=128)
    information = models.CharField(max_length=200,default='NULL')

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name


class Img(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    img = models.ImageField(upload_to='img')
    book = models.ForeignKey(medicine, on_delete=models.CASCADE)

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name


