#customauthentication/models.py extends the default django user model
from django.db import models


# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUserAuthentication(AbstractUser):
    """
    #add additional fields in here
    #email = models.EmailField(max_length=254, unique=True)
    #username = models.CharField(max_length=254, unique=True)
    #password = models.CharField(max_length=254, unique=True)
    #first_name = models.CharField(max_length=254, unique=True)
    #last_name = models.CharField(max_length=254, unique=True)
    #is_staff = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=False)
    #is_superuser = models.BooleanField(default=False)
    #last_login = models.DateTimeField(null=True, blank=True)
    #date_joined = models.DateTimeField(auto_now_add=True)
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['username', 'password', 'first_name', 'last_name']
    #def __str__(self):
    #    return self.email
    """
    pass
