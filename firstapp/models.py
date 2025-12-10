from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.TextField()


    def __str__(self):
        return self.title
class Standard(models.Model):
    name=models.CharField(max_length=100)
        
class Students(models.Model):
    name=models.CharField(max_length=200)
    std=models.ForeignKey(Standard,on_delete=models.CASCADE)