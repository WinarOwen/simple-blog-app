from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('',views.home,name='home'),
    path('create_post/',views.create_blog,name='create_blog'),
    path('view_post',views.view_blog,name='view_blog'),
    
]