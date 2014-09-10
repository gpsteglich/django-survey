from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from dynamicForms.fields import JSONField, STATUS, DRAFT
from dynamicForms import fields


class Form(models.Model):
    """
    Forms of the app.
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    status = models.IntegerField(choices=STATUS, default=DRAFT)
    publish_date = models.DateField(blank=True)
    expiry_date = models.DateField(blank=True)
    version = models.IntegerField(default=1)
    owner = models.ForeignKey('auth.User', related_name='forms', blank=True)
    json = JSONField(default="", blank=True)
    
    def save(self, *args, **kwargs):
        """
        Check if the slug is unique before saving a form.
        Throws ValidationError if the slug already exists.
        """
        self.slug = slugify(self.title)
        if Form.objects.filter(slug=self.slug).exists():
            raise ValidationError("Slug already exists. Choose another title.")
        super(Form,self).save(*args, **kwargs)
        
    class Meta:
        ordering = ('title',)
        

class Field(models.Model):
    """
    Fields of the forms.
    """
    label = models.CharField("Question", max_length=100)
    slug = models.SlugField(unique=True)
    field_type = models.IntegerField("Type", choices=fields.NAMES)
    required = models.BooleanField("Required", default=True)
    choices = models.CharField("Choices", max_length=200, blank=True,
            help_text="Por ahora opciones separadas por comas.")
    default = models.CharField("Default value", blank=True, max_length=100)
    help_text = models.CharField("Help text", blank=True, max_length=100)

    form = models.ForeignKey("Form", related_name="fields")

    class Meta:
        verbose_name = "Field"

    def __str__(self):
        return str(self.label)

    def get_choices(self):
        """
        Parse a comma separated choice string into a list of choices taking
        into account quoted choices using the ``settings.CHOICES_QUOTE`` and
        ``settings.CHOICES_UNQUOTE`` settings.
        """
        choice = ""
        quoted = False
        for char in self.choices:
            if not quoted and char == settings.CHOICES_QUOTE:
                quoted = True
            elif quoted and char == settings.CHOICES_UNQUOTE:
                quoted = False
            elif char == "," and not quoted:
                choice = choice.strip()
                if choice:
                    yield choice, choice
                choice = ""
            else:
                choice += char
        choice = choice.strip()
        if choice:
            yield choice, choice

class FormEntry(models.Model):
    form = models.ForeignKey("Form", related_name="entries")


class FieldEntry(models.Model):
    entry = models.ForeignKey("FormEntry", related_name="fields")

