from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,unique=True)
    birth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)


class UserInfo(models.Model):
    user = models.OneToOneField(User,unique=True)
    school = models.CharField(max_length=100,blank=True)
    company = models.CharField(max_length=100,blank=True)
    profession = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return "user:{}".format(self.user.username)

class A(models.Model):
    name= models.CharField('名称', max_length=32)

class B(models.Model):
    a= models.ForeignKey(A, verbose_name='A类',related_name = "test")
    name = models.CharField('称呼', max_length=16)
