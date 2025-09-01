# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    is_admin = forms.BooleanField(
        required=False,
        label='Register as Admin'
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_admin')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make email optional if needed
        self.fields['email'].required = False

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = self.cleaned_data.get('is_admin', False)
        if commit:
            user.save()
        return user