from django.db import models


import django
import uuid
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class loginModel(models.Model):
    username = models.CharField(max_length= 150)
    password = models.CharField(max_length=150)


def pic(instance, filename):
    return '/{0}/contactpics/{1}/{2}'.format(instance.user.username, instance.first_name, filename)

class Person(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=300, help_text = 'enter your contacts first name')
    last_name = models.CharField(max_length = 100, help_text = 'enter your contacts last name')
    middle_name = models.CharField(max_length = 100, help_text = 'enter your middle name')
    photo = models.ImageField(upload_to=pic, null=True)
    status = (
                ('M', 'Male'),
                ('F', 'Female'),
              )
    Gender = models.CharField(max_length=1, blank= True, choices=status, help_text='Gender')
    
class Contact(models.Model):
    contactee= models.ForeignKey(Person, null = True, on_delete=models.CASCADE )
    Tel_Number = models.CharField(max_length=10, help_text='mobile Number', unique= True)
    Address = models.CharField(max_length=250, help_text='Digital Address without hyphens')
    
    


