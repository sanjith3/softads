# dashboard/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def redirect_dashboard(request):
    if request.user.is_admin:
        return redirect('approvals:admin_dashboard')
    else:
        return redirect('enquiries:user_dashboard')