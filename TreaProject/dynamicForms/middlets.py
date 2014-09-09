from django.http import Http404
from django.core.exceptions import ValidationError

class ValidationErrorToHttpErrorMiddleware(object):
    def process_exception(self, request, exception):
        if isinstance(exception, ValidationError):
            raise Http404(exception.message)
