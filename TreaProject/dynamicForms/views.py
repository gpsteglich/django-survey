
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from dynamicForms.models import Form
from dynamicForms.serializers import FormSerializer, UserSerializer, NewFormSerializer

        #=======================================================================
        # try:
        #     p = Form.objects.get(slug=obj.slug)
        #     if p != None:
        #         raise Http404
        # except DoesNotExist: pass
        #=======================================================================
        # try:
        #     obj = Form.objects.get(slug=self.slug)
        #     if obj != None:
        #         raise ValidationError("mensajederoor")
        # except Form.DoesNotExist:
        #=======================================================================
        #=======================================================================

class FormList(generics.CreateAPIView):
    queryset = Form.objects.all()
    serializer_class =  NewFormSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
    
    
class FormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

