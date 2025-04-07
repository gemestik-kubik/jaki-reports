from django.urls import path
from .views import predict_report, predict_form

urlpatterns = [
    path('predict/', predict_report, name='predict_report'),         # API endpoint
    path('predict/form/', predict_form, name='predict_form'),        # Page for form input
]
