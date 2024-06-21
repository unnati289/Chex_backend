from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['static_id','ai_image', 'ai_text']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['original_image','ai_image', 'ai_text','doctor_comments']