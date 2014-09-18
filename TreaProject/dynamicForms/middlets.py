from django.core.exceptions import ValidationError
from django.http import Http404

from rest_framework import status
from rest_framework.renderers import JSONRenderer, YAMLRenderer
from rest_framework.response import Response

from .views import JSONResponse


class ValidationErrorToHttpErrorMiddleware(object):
     """
     Catch ValidationError exceptions and render them as JSONResponse
     """    
     def process_exception(self, request, exception):
        if isinstance(exception, ValidationError):
            content = {'error': exception.message}
            return JSONResponse(content)
