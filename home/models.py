from django.db import models

# Create your models here.
class User(models.Model):
   name = models.CharField(max_length=255, null=True)
   email = models.EmailField(max_length=255, null=True)
   phone = models.CharField(max_length=255, null=True)
   age = models.IntegerField(null=True)
   profile = models.FileField(null=True)

class Account(models.Model):
   name = models.CharField(max_length=255, null=True)
   email = models.EmailField(max_length=255)
   number = models.CharField(max_length=255)
   address = models.CharField(max_length=255)
   ifsc_code = models.IntegerField()


