
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
    (TEXT, _("Single line text")),
    (TEXTAREA, _("Multi line text")),
    (EMAIL, _("Email")),
    (NUMBER, _("Number")),
    (URL, _("URL")),
    (CHECKBOX, _("Check box")),
    (CHECKBOX_MULTIPLE, _("Check boxes")),
    (SELECT, _("Drop down")),
    (SELECT_MULTIPLE, _("Multi select")),
    (RADIO_MULTIPLE, _("Radio buttons")),
    (DATE, _("Date")),
    (CEDULA, _("Cedula")),
)

# Corresponding classes for each field type
CLASSES = {
    TEXT: forms.CharField,
    TEXTAREA: forms.CharField,
    EMAIL: forms.EmailField,
    CHECKBOX: forms.BooleanField,
    CHECKBOX_MULTIPLE: forms.MultipleChoiceField,
    SELECT: forms.ChoiceField,
    SELECT_MULTIPLE: forms.MultipleChoiceField,
    RADIO_MULTIPLE: forms.ChoiceField,
    DATE: forms.DateField,
    NUMBER: forms.FloatField,
    URL: forms.URLField,
}

FIELD_FILES = {
    TEXT: 'TextField',
    TEXTAREA: 'CharField',
    EMAIL: 'EmailField',
    CHECKBOX: 'BooleanField',
    CHECKBOX_MULTIPLE: 'MultipleChoiceField',
    SELECT: 'ChoiceField',
    SELECT_MULTIPLE: 'MultipleChoiceField',
    RADIO_MULTIPLE: 'ChoiceField',
    DATE: 'DateField',
    NUMBER: 'FloatField',
    URL: 'URLField',
    CEDULA: 'CIField',
}

TEMPLATES = {
    TEXT: 'question_char.html',
    TEXTAREA: 'question_text_area.html',
    EMAIL: 'field_mail.html',
    CHECKBOX: 'BooleanField',
    CHECKBOX_MULTIPLE: 'MultipleChoiceField',
    SELECT: 'field_combobox.html',
    SELECT_MULTIPLE: 'field_combobox.html',
    RADIO_MULTIPLE: 'ChoiceField',
    DATE: 'DateField',
    NUMBER: 'question_num.html',
    URL: 'URLField',
    CEDULA: 'field_identityDoc.html',
}
