
from django.utils.translation import ugettext_lazy as _
from django import forms
#field type constants
# TODO these are not necessarily those we need. 
TEXT = 1
TEXTAREA = 2
EMAIL = 3
CHECKBOX = 4
CHECKBOX_MULTIPLE = 5
SELECT = 6
SELECT_MULTIPLE = 7
RADIO_MULTIPLE = 8
DATE = 9
NUMBER = 10
URL = 11
CEDULA = 12


#These are the field types.
NAMES = (
    (TEXT, "Single line text"),
    (TEXTAREA, "Multi line text"),
    (EMAIL, "Email"),
    (NUMBER, "Number"),
    #(URL, "URL"),
    (CHECKBOX, "Check box"),
    #(CHECKBOX_MULTIPLE, "Check boxes"),
    (SELECT, "Drop down"),
    #(SELECT_MULTIPLE, "Multi select"),
    #(RADIO_MULTIPLE, "Radio buttons"),
    #(DATE, "Date"),
    (CEDULA, "Cedula"),
)


FIELD_FILES = {
    TEXT: 'dynamicForms.fieldtypes.TextField',
    TEXTAREA: 'dynamicForms.fieldtypes.TextAreaField',
    EMAIL: 'dynamicForms.fieldtypes.EmailField',
    CHECKBOX: 'dynamicForms.fieldtypes.BooleanField',
    CHECKBOX_MULTIPLE: 'dynamicForms.fieldtypes.MultipleChoiceField',
    SELECT: 'dynamicForms.fieldtypes.ChoiceField',
    SELECT_MULTIPLE: 'dynamicForms.fieldtypes.MultipleChoiceField',
    RADIO_MULTIPLE: 'dynamicForms.fieldtypes.ChoiceField',
    DATE: 'dynamicForms.fieldtypes.DateField',
    NUMBER: 'dynamicForms.fieldtypes.NumberField',
    URL: 'dynamicForms.fieldtypes.URLField',
    CEDULA: 'dynamicForms.fieldtypes.CIField',
}
'''
TEMPLATES = {
    TEXT: 'fields/text/template.html',
    TEXTAREA: 'fields/text_area/template.html',
    EMAIL: 'fields/email/template.html',
    CHECKBOX: 'fields/checkbox/template.html',
    CHECKBOX_MULTIPLE: 'MultipleChoiceField',
    SELECT: 'fields/combobox/template.html',
    SELECT_MULTIPLE: 'fields/combobox/template.html',
    RADIO_MULTIPLE: 'ChoiceField',
    DATE: 'DateField',
    NUMBER: 'fields/number/template.html',
    URL: 'URLField',
    CEDULA: 'fields/identity_doc/template.html',
}

FIELD_PRP_TEMP = {
    TEXT: 'fields/text/properties.html',
    TEXTAREA: 'fields/text_area/properties.html',
    EMAIL: 'fields/email/properties.html',
    CHECKBOX: 'fields/checkbox/properties.html',
    CHECKBOX_MULTIPLE: 'MultipleChoiceField',
    SELECT: 'fields/combobox/properties.html',
    SELECT_MULTIPLE: 'fields/combobox/properties.html',
    RADIO_MULTIPLE: 'ChoiceField',
    DATE: 'DateField',
    NUMBER: 'fields/number/properties.html',
    URL: 'URLField',
    CEDULA: 'fields/identity_doc/properties.html',
}
'''
