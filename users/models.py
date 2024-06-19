from django.db import models
import uuid
from django.core.validators import RegexValidator
from datetime import date

SEX_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

# Create your models here.
class User(models.Model):
    static_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auth_user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True, validators=[RegexValidator(r'^\w+@\w+\.\w{2,3}$')])
    mobile_num = models.CharField(max_length=10, unique=True, validators=[RegexValidator(r'^\d{1,10}$')])
    dob = models.DateField(null=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=False)
    address = models.TextField(null=True)
    pincode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,6}$')])

    @property
    def age(self):
        return date.today().year - self.dob.year
    
class Patient(User):
    medication = models.TextField(null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)

class Doctor(User):
    about = models.TextField(null=True)
    description = models.TextField(null=True)
