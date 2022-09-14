from distutils.command.upload import upload
from django.db import models

class Employee(models.Model):
    
    
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=20)
    salary = models.IntegerField(max_length=20)
    qualification = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

