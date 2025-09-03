# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    list_display = ('username', 'mobile_number', 'email', 'is_admin', 'is_staff')
    list_filter = ('is_admin', 'is_staff')
    search_fields = ('username', 'email', 'mobile_number')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mobile_number', 'is_admin')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('mobile_number', 'is_admin')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)