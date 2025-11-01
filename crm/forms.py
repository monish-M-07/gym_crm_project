from django import forms
from .models import Member, FeePayment

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone', 'membership_type']

class FeePaymentForm(forms.ModelForm):
    class Meta:
        model = FeePayment
        fields = ['member', 'amount', 'payment_date', 'next_due_date']
