from django.shortcuts import render
from dynamicForms import views

from formularios.models import Usuario
from formularios.serializer import UsuarioSerializer

from rest_framework import generics
from rest_framework import permissions
from rest_framework import status

class UserList(generics.ListCreateAPIView):
    """
    APIView where the forms of the app are listed and a new form can be added.
    """
    model = Usuario
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    APIView to see details, modify or delete a form.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)







# Create your views here.
