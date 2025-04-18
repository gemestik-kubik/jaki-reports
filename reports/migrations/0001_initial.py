# Generated by Django 5.1.5 on 2025-04-04 23:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('content', models.TextField()),
                ('category_name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_privacy', models.BooleanField(default=False)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='diajukan', max_length=20)),
                ('predicted_zone_name', models.CharField(blank=True, max_length=200, null=True)),
                ('confidence_score', models.FloatField(blank=True, null=True)),
                ('actual_zone_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
