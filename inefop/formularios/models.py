from django.db import models

from dynamicForms.fieldtypes import FieldFactory
# Create your models here.


class Usuario(models.Model):
    name = models.TextField(max_length=20)
    surname = models.TextField(max_length=20)
    birthdate = models.DateField()
    has_car = models.BooleanField()

    def __str__(self):
        return name + surname


FieldFactory.FieldFactory.register_model('Usuario', Usuario)


class Country(models.Model):
    name = models.TextField(max_length=30)

    def __str__(self):
        return name
    

class Club(models.Model):
    name = models.TextField(max_length=30)
    country = models.ForeignKey(Country, related_name='clubs')
    established = models.DateField()

    def __str__(self):
        return name +'(' + country.__str__() + ')'


FieldFactory.FieldFactory.register_model('Club', Club)
