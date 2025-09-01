# approvals/urls.py
from django.urls import path
from . import views

app_name = 'approvals'

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update-status/<int:enquiry_id>/', views.update_enquiry_status, name='update_status'),

]