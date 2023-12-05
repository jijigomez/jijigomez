from django.db import models

# Create your models here.
# import the standard Django Model
# from built-in library
class LoginModel(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()