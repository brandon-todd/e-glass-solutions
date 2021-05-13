from django.shortcuts import render
from .forms import CustomerTabs
# Create your views here.
def customers(request):
    if request.method != 'POST':
        form = CustomerTabs
    else:
        form = CustomerTabs(data=request.POST)
        if form.is_valid():
            form.save()
        return render(request,'index.html')
    context={'form':form}    
    return render(request,'customer.html',context)