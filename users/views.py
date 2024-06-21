from rest_framework import generics
from .models import User
from .serializers import UserSerializer,PatientSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404
import uuid

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'static_id'
    
    def get_object(self):
        static_id = self.kwargs['static_id']
        try:
            uuid_obj = uuid.UUID(str(static_id))
        except ValueError:
            raise Http404("Invalid UUID format")

        return get_object_or_404(User, static_id=uuid_obj)
    
class PatientDetailView(generics.RetrieveAPIView):
    serializer_class = PatientSerializer
    lookup_field = 'static_id'
    
    def get_object(self):
        static_id = self.kwargs['static_id']
        try:
            uuid_obj = uuid.UUID(str(static_id))
        except ValueError:
            raise Http404("Invalid UUID format")

        return get_object_or_404(User, static_id=uuid_obj)