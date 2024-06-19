import uuid
from django.db import models
from users.models import *

# Create your models here.
class Image(models.Model):
    static_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False)
    original_image = models.ImageField(upload_to='media/images/original', null=False)
    ai_text = models.TextField(null=True)
    ai_image = models.ImageField(upload_to='media/images/ai', null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    doctor_comments = models.TextField(null=True)

    def __str__(self):
        return f"{self.patient.name} - {self.date_added}"