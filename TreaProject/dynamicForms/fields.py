from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import ugettext_lazy as _

import json

from south.modelsinspector import add_introspection_rules


#form status constants
DRAFT = 0
PUBLISHED = 1
EXPIRED = 2
#These are the possible status for a form
STATUS = (
          (DRAFT, _("Draft")),
          (PUBLISHED, _("Published")),
          (EXPIRED, _("Expired")),
          )

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

