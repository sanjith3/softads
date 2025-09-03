# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    mobile_number = forms.CharField(label='Mobile number', help_text='Enter 10 digits')
    is_admin = forms.BooleanField(required=False, label='Register as Admin')

    class Meta:
        model = CustomUser
        fields = ('username', 'mobile_number', 'email', 'password1', 'password2', 'is_admin')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = False

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = self.cleaned_data.get('is_admin', False)
        user.mobile_number = ''.join(ch for ch in self.cleaned_data['mobile_number'] if ch.isdigit())[-10:]
        if commit:
            user.save()
        return user