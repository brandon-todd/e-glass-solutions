from django.urls import path,include
from . import views
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
app_name = 'users'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',LoginView.as_view(template_name='login.html'),name = 'login'),
    path('signup',views.SignUp, name = 'signup'),
    path('logout/',views.logout_view,name ='logout'),
]