from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify

from dynamicForms.fields import JSONField, STATUS, DRAFT, PUBLISHED
from datetime import date


class Form(models.Model):
    """
    Forms of the app.
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey('auth.User', related_name='forms', blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """
        Check if the slug is unique before saving a form.
        If there such a slug it checks if it is the same form.
        Throws ValidationError if the slug already exists.
        """
        self.slug = slugify(self.title)
        if Form.objects.filter(slug=self.slug).exists():
            # If it is an update it will enter here
            # Or if I try to create a new form with an conflicting slug
            f1 = Form.objects.get(slug=self.slug)
            if (self.pk != f1.pk):
                raise ValidationError("Slug already exists. Choose another title.")
        super(Form,self).save(*args, **kwargs)
        
        
    class Meta:
        ordering = ('title',)
        
        
class Version(models.Model):
    number = models.IntegerField(default=1)
    json = JSONField(default="", blank=True)
    status = models.IntegerField(choices=STATUS, default=DRAFT)
    publish_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    form = models.ForeignKey("Form", related_name="versions")
    
    def __str__(self):
        return str(self.number)
    #'%d: %s' % (self.number, self.get_status_display())
    
    def save(self, *args, **kwargs):
        
        #if (self.number < 1):
        #   raise ValidationError("Version cannot be below 1.")
        if Version.objects.filter(pk=self.pk).exists():
            #When it's an update of an existing version
            pass
        else:
            #When it's a POST of a new Version
            # if it is a new version of an existing form
            # check if there is no previous draft and
            # check that there exists a version less than the current
            all_versions = self.form.versions.all()  
            count = all_versions.count()
            if (count > 0):
                #if it is the first version do not check any of these
                if not all_versions.filter(number=count).exists():
                    # We consider all the previous versions have to exist.
                    # There would be a severe problem if the admin touches the database to delete a old version.
                    raise ValidationError("Oops. There is a problem with the version" 
                                          "numbers. The previous version does not exist.")
                if (all_versions.get(number=count).status == DRAFT):
                    raise ValidationError('There is a previous draft pending for this Form')
                self.number = all_versions.count() + 1
        if (self.status == PUBLISHED):
            self.publish_date = date.today()
        super(Version,self).save(*args, **kwargs)


class FormEntry(models.Model):
    version = models.ForeignKey("Version", related_name="entries")
    entry_time = models.DateField(blank=True)



class FieldEntry(models.Model):
    field_id = models.IntegerField()
    field_type = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    required = models.BooleanField()
    answer = models.CharField(max_length=200)
    entry = models.ForeignKey("FormEntry", related_name="fields", blank=True, null=True)

    def __str__(self):
        return '%s : %s' % (self.text, self.answer)