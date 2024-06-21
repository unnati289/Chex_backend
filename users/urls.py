from django.urls import path
from .views import UserDetailView,PatientDetailView

urlpatterns = [
    path('user_details/<uuid:static_id>/', UserDetailView.as_view(), name='user-details'),
    path('patient_details/<uuid:static_id>/', PatientDetailView.as_view(), name='patient-details'),
]