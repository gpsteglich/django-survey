from django.core.exceptions import ValidationError


class FieldFactory():
    #factory

    fields = {}
    models = {}

    def get_class(id):
        return FieldFactory.fields[id]

    def get_model_class(id):
        return FieldFactory.models[id]

    def register(id, type):
        if id not in FieldFactory.fields:
            FieldFactory.fields[id] = type
        else:
            raise ValidationError("invalid ID.")

    def register_model(id, type):
        if id not in FieldFactory.models:
            FieldFactory.models[id] = type
        else:
            raise ValidationError("invalid ID.")

    def get_strings():
        l = {}
        for key in FieldFactory.fields:
            l[key] = FieldFactory.fields[key]().__str__()
        return l

    def get_model_strings():
        l = {}
        for key in FieldFactory.models:
            l[key] = FieldFactory.models[key].__str__()
        return l