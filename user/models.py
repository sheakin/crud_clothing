from django.db import models

# Create your models here.
class A_User(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=100)
    email=models.EmailField()


