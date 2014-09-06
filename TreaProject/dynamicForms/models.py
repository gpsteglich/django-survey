from django.db import models
from dynamicForms.fields import JSONField, STATUS

class Form(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    status = models.IntegerField(choices=STATUS)
    publish_date = models.DateField()
    expiry_date = models.DateField()
    version = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='forms', blank=True)
    json = JSONField(default="", blank=True)
    
    
    class Meta:
        ordering = ('title',)
        
