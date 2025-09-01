# dashboard/urls.py
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.redirect_dashboard, name='redirect_dashboard'),
]