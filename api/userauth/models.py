from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True, max_length=200)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200)
    otp = models.CharField(unique=True, max_length=100)
    data_added = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        email_username, full_name = self.email.split('@')
        if self.full_name == '' or self.full_name == None:
            self.full_name = email_username
        if self.username == '' or self.username == None:
            self.username = email_username
        super(User, self).save(*args, **kwargs)
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to='user_folder', default='default_user.jpg', null=True, blank=True)
    full_name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    about = models.TextField(null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.full_name:
            return self.full_name
        else:
            return str(self.user.full_name)   
    


