from django.db import models
from dynamicForms.fields import JSONField, NAMES

class Form(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=35)
    status = models.IntegerField(choices=NAMES)
    publish_date = models.DateField()
    expiry_date = models.DateField()
    version = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='forms', default='1')
    json = JSONField(max_length=1000, default="", blank=True)
    
    
    class Meta:
        ordering = ('title',)
        
