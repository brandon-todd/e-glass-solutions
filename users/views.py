from django.shortcuts import render,redirect 
from django.contrib.auth import login,logout,authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
# Create your views here.

def index(request):
    return render(request, 'index.html')
def SignUp(request):
    if request.method != 'POST':
        form = CustomUserCreationForm
    else:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
        return render(request,'index.html')
    context={'form':form}    
    return render(request,'signup.html',context)

def logout_view(request):
    logout(request)
    return redirect('users:index')