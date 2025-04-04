from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at', 'status', 'predicted_zone_name')
    search_fields = ('code', 'content', 'predicted_zone_name')
