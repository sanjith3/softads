# enquiries/urls.py
from django.urls import path
from . import views

app_name = 'enquiries'

urlpatterns = [
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
]