from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class BlogForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']