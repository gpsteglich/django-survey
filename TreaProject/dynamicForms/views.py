from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from dynamicForms.models import Form
from dynamicForms.serializers import FormSerializer, UserSerializer


class FormList(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class =  FormSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
    
class FormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

