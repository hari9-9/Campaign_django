from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import points

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            p = points(username=username, points=0)
            p.save()
            form.save()
            # messages.success(request,f'Your account has been created! you are now able to log in')
            return redirect('mysite-home')

    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})


