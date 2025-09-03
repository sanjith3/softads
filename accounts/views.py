# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django import forms
from .forms import CustomUserCreationForm


class MobileLoginForm(forms.Form):
    username = forms.CharField(label='Mobile number')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_username(self):
        value = self.data.get('username', '')
        if value is None:
            return ''
        digits = ''.join(ch for ch in value if ch.isdigit())
        return digits[-10:]

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            auth_user = authenticate(request, username=user.username, password=raw_password)
            if auth_user is None and getattr(user, 'mobile_number', None):
                auth_user = authenticate(request, mobile_number=user.mobile_number, password=raw_password)
            if auth_user is not None:
                login(request, auth_user)
            return redirect('dashboard:redirect_dashboard')
        else:
            # Print form errors to console for debugging
            print("Form errors:", form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = MobileLoginForm(request.POST)
        if form.is_valid():
            mobile_clean = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # First try mobile-number authentication using the cleaned 10-digit value
            user = authenticate(request, mobile_number=mobile_clean, password=password)
            # Fallback: try Django's default username auth in case user typed username
            if user is None:
                user = authenticate(request, username=mobile_clean, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:redirect_dashboard')
        else:
            # Print form errors to console for debugging
            print("Login form errors:", form.errors)
    else:
        form = MobileLoginForm()
    return render(request, 'accounts/login.html', {'form': form})