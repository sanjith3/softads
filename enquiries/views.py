# enquiries/views.py
from django.shortcuts import render, redirect  # Add redirect to the import
from django.contrib.auth.decorators import login_required
from .models import Enquiry
from .forms import EnquiryForm


@login_required
def user_dashboard(request):
    enquiries = Enquiry.objects.filter(user=request.user).order_by('-created_at')

    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.user = request.user
            enquiry.save()
            return redirect('enquiries:user_dashboard')
    else:
        form = EnquiryForm()

    return render(request, 'enquiries/user_dashboard.html', {
        'form': form,
        'enquiries': enquiries
    })