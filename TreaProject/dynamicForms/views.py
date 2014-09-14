
from django.contrib.auth.models import User
from django.http import HttpResponse

from dynamicForms.models import Form,FormEntry
from dynamicForms.serializers import FormSerializer, UserSerializer, NewFormSerializer,FieldEntrySerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class FormList(generics.ListCreateAPIView):
    """
    APIView where the forms of the app are listed and a new form can be added.
    """
    queryset = Form.objects.all()
    serializer_class =  NewFormSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user

class FormCreate(generics.CreateAPIView):
    """
    APIView to see details, modify or delete a form.
    """
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (permissions.AllowAny,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user

class FormDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    APIView to see details, modify or delete a form.
    """
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (permissions.AllowAny,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
        

class UserList(generics.ListAPIView):
    """
    APIView listing the users of the app.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    APIView showing basic details about the users of the app.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

                
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['POST'])
def submit_form_entry(request, slug):
    """
    APIView to submit a Form Entry.
    """
    entry = FormEntry(form=Form.objects.get(slug=slug))  
    for field in request.DATA:
            serializer = FieldEntrySerializer(data=field)
            serializer.object.entry = entry
            if serializer.is_valid():
                serializer.save()
