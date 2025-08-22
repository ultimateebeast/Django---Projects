# checker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_number, name='check_number'),
]