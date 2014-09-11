from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils import simplejson as json
from django.utils.translation import ugettext_lazy as _
from south.modelsinspector import add_introspection_rules

#field type constaants
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

#form status constants
DRAFT = 0
PUBLISHED = 1
#These are the possible status for a form
STATUS = (
          (DRAFT, _("Draft")),
          (PUBLISHED, _("Published")),
          )


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

add_introspection_rules([], ["^dynamicForms.fields.JSONField"])

class JSONField(models.TextField):
    """JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly"""

    # Used so to_python() is called
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        """Convert our string value to JSON after we load it from the DB"""

        if value == "":
            return ""

        try:
            if isinstance(value, str):
                return json.loads(value)
        except ValueError:
            pass

        return ""

    def get_db_prep_save(self, value, connection, prepared=False):
        """Convert our JSON object to a string before we save"""


        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)

        return super(JSONField, self).get_db_prep_save(value, connection)

