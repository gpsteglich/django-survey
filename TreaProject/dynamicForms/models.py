from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from dynamicForms.fields import JSONField, STATUS, DRAFT


class Form(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    status = models.IntegerField(choices=STATUS, default=DRAFT)
    publish_date = models.DateField(blank=True)
    expiry_date = models.DateField(blank=True)
    version = models.IntegerField(default=1)
    owner = models.ForeignKey('auth.User', related_name='forms', blank=True)
    json = JSONField(default="", blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        try:
             obj = Form.objects.get(slug=self.slug)
             if obj != None:
                 raise ValidationError("mensajederror")
        except Form.DoesNotExist:
            super(Form,self).save(*args, **kwargs)
        
    class Meta:
        ordering = ('title',)
        
