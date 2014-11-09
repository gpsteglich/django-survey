from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify

from dynamicForms.fields import JSONField, STATUS, DRAFT, PUBLISHED, EXPIRED
from datetime import datetime


from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
import json

class VersionQueySet(models.query.QuerySet):
    """
    QuerySet for Version model
    """
    def data_icontains(self, *args, **kwargs):
        entries = self.get(pk=kwargs['version']).entries.all()
        data = []
        for entry in entries:
            fields = entry.fields.filter(field_id=kwargs['field_id'], answer__icontains=kwargs['data'])
            # for field in fields:
            if fields.count() > 0:
                for field in entry.fields.all():
                    data.append(field)
        return data
    def data_iexact(self, *args, **kwargs):
        entries = self.get(pk=kwargs['version']).entries.all()
        data = []
        for entry in entries:
            fields = entry.fields.filter(field_id=kwargs['field_id'], answer__iexact=kwargs['data'])
            # for field in fields:
            if fields.count() > 0:
                for field in entry.fields.all():
                    data.append(field)
        return data
    def data_all(self, *args, **kwargs):
        entries = self.get(pk=kwargs['version']).entries.all()
        data = []
        for entry in entries:
            fields = entry.fields.filter(field_id=kwargs['field_id'])
            # for field in fields:
            if fields.count() > 0:
                for field in entry.fields.all():
                    data.append(field)
        return data


class VersionManager(models.Manager):
    """
    Manager for Version model
    """
    def get_queryset(self):
        return VersionQueySet(self.model, using=self._db)


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
                raise ValidationError("Slug already exists."
                " Choose another title.")
        super(Form, self).save(*args, **kwargs)

    class Meta:
        ordering = ('title',)


class Version(models.Model):
    number = models.IntegerField(default=1)
    json = JSONField(default="", blank=True)
    status = models.IntegerField(choices=STATUS, default=DRAFT)
    publish_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    form = models.ForeignKey("Form", related_name="versions")

    objects = VersionManager()

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
                    # There would be a severe problem if the admin
                    # touches the database to delete a old version.
                    raise ValidationError("Oops. There is a problem with the "
                    "version numbers. The previous version does not exist.")
                if (all_versions.get(number=count).status == DRAFT):
                    raise ValidationError("There is a previous draft "
                    "pending for this Form")
                self.number = all_versions.count() + 1
        if (self.status == PUBLISHED) and (self.publish_date is None):
            self.publish_date = datetime.now()
            # If there is a previous published version,
            # its status is changed to expired.
            prev_versions = self.form.versions.filter(status=PUBLISHED)
            if len(prev_versions) > 0:
                # We assume there can only be one published version at any time
                prev = prev_versions.first()
                prev.status = EXPIRED
                prev.expiry_date = datetime.now()
                super(Version, prev).save()
        elif (self.publish_date is not None):
            raise ValidationError('You cannot edit a published form')
        super(Version, self).save(*args, **kwargs)

class FormEntry(models.Model):
    version = models.ForeignKey("Version", related_name="entries")
    entry_time = models.DateTimeField(blank=True)
    

@receiver(post_save, sender=FormEntry)
def notification_mail(sender, **kwargs):
    instance = kwargs.get('instance')
    js = instance.version.json
    d = json.loads(js)
    if d['after_submit']['sendMail']:
        content = d['after_submit']['mailText']
        subject = d['after_submit']['mailSubject']
        sender = d['after_submit']['mailSender']
        
        print(content)
        try:
            send_mail(subject, content, sender, ['santrbl@gmail.com'], fail_silently=False)
        except Exception as e:
            print ("ERROR")



class FieldEntry(models.Model):
    field_id = models.IntegerField()
    field_type = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    required = models.BooleanField()
    shown = models.BooleanField(default=True)
    answer = models.CharField(max_length=200, blank=True, null=True)
    entry = models.ForeignKey("FormEntry", related_name="fields",
                             blank=True, null=True)

    def __str__(self):
        return '%s : %s' % (self.text, self.answer)
