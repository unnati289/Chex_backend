# views.py
from rest_framework import generics
from .models import Image
from .serializers import ImageSerializer, ReportSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404
from users.models import User
import uuid
class ReportListView(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        patient_static_id = self.kwargs['patient_static_id']
        try:
            patient = get_object_or_404(User, static_id=patient_static_id)
        except ValueError:
            raise Http404("Invalid UUID format")

        return Image.objects.filter(patient__static_id=patient_static_id)
    
class ReportView(generics.RetrieveAPIView):
    serializer_class = ReportSerializer
    lookup_field = 'static_id'
    
    def get_object(self):
        static_id = self.kwargs['static_id']
        try:
            uuid_obj = uuid.UUID(str(static_id))
        except ValueError:
            raise Http404("Invalid UUID format")

        return get_object_or_404(Image, static_id=uuid_obj)