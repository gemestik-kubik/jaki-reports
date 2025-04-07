from django.urls import path
from .views import predict_report, predict_form

urlpatterns = [
    path('', predict_report, name='predict_report'),         # API endpoint
    path('form/', predict_form, name='predict_form'),        # Page for form input
]
