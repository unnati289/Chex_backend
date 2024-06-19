# Generated by Django 5.0.6 on 2024-06-19 09:22

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('static_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('original_image', models.ImageField(upload_to='media/images/original')),
                ('ai_text', models.TextField(null=True)),
                ('ai_image', models.ImageField(null=True, upload_to='media/images/ai')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('doctor_comments', models.TextField(null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
        ),
    ]