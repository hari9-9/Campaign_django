from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Points

# Create your views here.

def register(request, uname=None):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            p = Points(username=username)
            p.save()
            form.save()
            if uname is not None:
                p = Points.objects.get(username=uname)
                p.points+=1
                p.save()

            print(uname)
            # messages.success(request,f'Your account has been created! you are now able to log in')
            return redirect('login')

    else:
        form = UserRegisterForm()
        print(uname)
    return render(request,'users/register.html',{'form': form})


@login_required
def profile(request):
    p = Points.objects.get(username=request.user.username)
    point = p.points
    url = "https:\\\\127.0.0.1:8000\\"+request.user.username
    context ={
        'username' : request.user.username,
        'points' : point,
        'url' : url
    }
    return render(request, 'users/profile.html', {'data':context})


