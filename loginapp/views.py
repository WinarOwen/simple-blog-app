from django.shortcuts import render,redirect
from .forms import Registration,BlogForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post
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

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request,'create_blog/create_blog.html',{'form':form})

def view_blog(request):
    blog_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(blog_list,5)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    return render(request,'view_blog/view_blog.html',{'blogs':blogs})

