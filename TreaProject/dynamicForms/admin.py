from django.contrib import admin

from dynamicForms.models import Form, FieldEntry, FormEntry, Field, Version


# Register your models here.
admin.site.register(Form)
admin.site.register(Field)
admin.site.register(FieldEntry)
admin.site.register(FormEntry)
admin.site.register(Version)