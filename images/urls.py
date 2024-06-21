from django.urls import path
from .views import ReportListView,ReportView

urlpatterns = [
    path('reports/<uuid:patient_static_id>/', ReportListView.as_view(), name='reports-list'),
    path('reports_details/<uuid:static_id>/', ReportView.as_view(), name='reports-list'),
]