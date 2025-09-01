# enquiries/admin.py
from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('ad_title', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('ad_title', 'user__username', 'name')