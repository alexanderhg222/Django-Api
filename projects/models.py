from errno import EDEADLK
from django.db import models

# Create your models here.
class Project(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=100)
    edad=models.IntegerField()
    fecha=models.DateTimeField(auto_now_add=True)