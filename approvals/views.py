# approvals/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from enquiries.models import Enquiry
from django import forms


def admin_check(user):
    return user.is_admin


class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['status', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


@login_required
@user_passes_test(admin_check)
def admin_dashboard(request):
    pending_enquiries = Enquiry.objects.filter(status='Pending').order_by('-created_at')
    approved_enquiries = Enquiry.objects.filter(status='Approved').order_by('-created_at')
    rejected_enquiries = Enquiry.objects.filter(status='Rejected').order_by('-created_at')

    return render(request, 'approvals/admin_dashboard.html', {
        'pending_enquiries': pending_enquiries,
        'approved_enquiries': approved_enquiries,
        'rejected_enquiries': rejected_enquiries,
    })


@login_required
@user_passes_test(admin_check)
def update_enquiry_status(request, enquiry_id):
    enquiry = get_object_or_404(Enquiry, id=enquiry_id)

    if request.method == 'POST':
        form = ApprovalForm(request.POST, instance=enquiry)
        if form.is_valid():
            form.save()
            return redirect('approvals:admin_dashboard')
    else:
        form = ApprovalForm(instance=enquiry)

    return render(request, 'approvals/update_status.html', {
        'form': form,
        'enquiry': enquiry
    })