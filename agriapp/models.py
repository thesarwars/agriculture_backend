from django.db import models

# Create your models here.
class UserLogin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)
    

class HomePageData(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    imageField = models.ImageField()