from django.urls import path
from .views import predict_report

urlpatterns = [
    path('predict/', predict_report, name='predict_report'),
]
