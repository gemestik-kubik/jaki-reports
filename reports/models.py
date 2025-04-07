import uuid
from django.db import models

class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=20, unique=True)
    image_url = models.URLField(blank=True, null=True)

    content = models.TextField()
    category_name = models.CharField(max_length=100, blank=True, null=True)
    is_privacy = models.BooleanField(default=False)
    
    latitude = models.FloatField()
    longitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="diajukan")

    predicted_zone_name = models.CharField(max_length=200, blank=True, null=True)
    confidence_score = models.FloatField(blank=True, null=True)

    actual_zone_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.content[:30]}"
