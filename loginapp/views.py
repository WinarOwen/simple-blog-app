from django.shortcuts import render,redirect
from .forms import Registration,BlogForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Registration()
    return render(request, 'register/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request,'login/login.html',{'form':form})

def home(request):
    return render(request,'home/home.html')
