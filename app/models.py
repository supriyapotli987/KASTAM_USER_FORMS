from typing import Any
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
class Userprofilemanager(BaseUserManager):
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('Enter the valid mail')
        NE=self.normalize_email(email)
        UO=self.model(email=NE,first_name=first_name,last_name=last_name)
        UO.set_password(password)
        UO.save()
        return UO
    def create_superuser(self,email,first_name,last_name,password):
        UO=self.create_user(email,first_name,last_name,password)
        UO.is_staff=True
        UO.is_superuser=True
        UO.save()


        










class Userprofile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']
    objects=Userprofilemanager()







