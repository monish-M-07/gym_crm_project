from django.shortcuts import render, redirect
from .models import Member, FeePayment
from .forms import MemberForm, FeePaymentForm

def dashboard(request):
    members = Member.objects.count()
    fees = FeePayment.objects.count()
    return render(request, 'crm/dashboard.html', {'members': members, 'fees': fees})

def members_list(request):
    members = Member.objects.all()
    return render(request, 'crm/members.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members_list')
    else:
        form = MemberForm()
    return render(request, 'crm/add_member.html', {'form': form})

def fees_list(request):
    fees = FeePayment.objects.all()
    return render(request, 'crm/fees.html', {'fees': fees})

def add_fee(request):
    if request.method == 'POST':
        form = FeePaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fees_list')
    else:
        form = FeePaymentForm()
    return render(request, 'crm/add_fee.html', {'form': form})
