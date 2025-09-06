from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('enquiries/', include('enquiries.urls')),
    path('approvals/', include('approvals.urls')),
    path('', RedirectView.as_view(url='/dashboard/', permanent=False)),
]
