from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['static_id', 'name', 'profile_pic']  

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['static_id', 'name','sex','height','weight','medication']
