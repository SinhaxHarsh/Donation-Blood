from django.shortcuts import render,redirect
from .forms import DonorForm
from.models import Donor

def home(request):
    return render(request,'index.html')

def registeration(request):
    if request.method=="POST":
        form= DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form= DonorForm()
        return render(request,'register.html')
    

def dashboard(request):
    donors= Donor.objects.all()
    context={'donor':donors}
    return render(request,'dashboard.html',context=context)