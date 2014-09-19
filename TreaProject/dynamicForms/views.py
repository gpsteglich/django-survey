
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from dynamicForms.models import Form,FormEntry, Version
from dynamicForms.serializers import FormSerializer, UserSerializer
from dynamicForms.serializers import FieldEntrySerializer
from dynamicForms.serializers import VersionSerializer


class FormList(generics.ListCreateAPIView):
    """
    APIView where the forms of the app are listed and a new form can be added.
    """
    model = Form
    queryset = Form.objects.all()
    serializer_class =  FormSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
      


class FormDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    APIView to see details, modify or delete a form.
    """
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
        
class VersionList(generics.ListCreateAPIView):
    """
    APIView where the forms of the app are listed and a new form can be added.
    """
    model = Version
    serializer_class =  VersionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, slug, format=None):
        versions = Form.objects.get(slug=slug).versions.all()
        serializer = VersionSerializer(versions, many=True)
        return Response(serializer.data)

    def post(self, request, slug, format=None):
        serializer = VersionSerializer(data=request.DATA)
        form = Form.objects.get(slug=slug)
        serializer.form = form
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class VersionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    APIView to see details, modify or delete a form.
    """
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get_object(self, slug, number):
        try:
            form = Form.objects.get(slug=slug)
            return form.versions.get(number=number)
        except Version.DoesNotExist or Form.DoesNotExist:
            raise Http404

    def get(self, request, slug, number, format=None):
        version = self.get_object(slug, number)
        serializer = VersionSerializer(version)
        return Response(serializer.data)

    def put(self, request, slug, number, format=None):
        version = self.get_object(slug, number)
        serializer = VersionSerializer(version, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,  slug, number, format=None):
        #version = self.get_object(slug, number)
        #version.delete()
        return Response(status=status.HTTP_403_FORBIDDEN)
           

                
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['POST'])
def submit_form_entry(request, slug, format=None):
    """
    APIView to submit a Form Entry.
    """
    # TODO: agregar primera iteracion por las respuestas
    # para hacer la validacion, antes de crear el entry
    '''
    for field in request.DATA:
            serializer = FieldEntrySerializer(data=field)
            #Validar campo
            #if not validar:
                #Enviar respuesta al front con el error
    '''
    entry = FormEntry(form=Form.objects.get(slug=slug))
    entry_time = datetime.now()
    entry.save() 
    for field in request.DATA:
            serializer = FieldEntrySerializer(data=field)
            serializer.object.entry_id = entry.id
            if serializer.is_valid():
                serializer.save()
    return Response(serializer.data)
