from django.db import models

# Create your models here.


class Usuario(models.Model):
    name = models.TextField(max_length=20)
    surname = models.TextField(max_length=20)
    birthdate = models.DateField()
    has_car = models.BooleanField()