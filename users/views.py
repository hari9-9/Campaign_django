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
    url = "http:\\\\127.0.0.1:8000\\"+request.user.username
    context ={
        'username' : request.user.username,
        'points' : point,
        'url' : url
    }
    return render(request, 'users/profile.html', {'data':context})

@login_required
def leaderboard(request):
    p=Points.objects.order_by("-points")[0:10]
    pe = Points.objects.get(username=request.user.username)

    t={
        'username' : p[0].username,
        'points' : p[0].points,
        'username1': p[1].username,
        'points1' : p[1].points,
        'username2': p[2].username,
        'points2' : p[2].points,
        'username3': p[3].username,
        'points3' : p[3].points,
        'username4': p[4].username,
        'points4' : p[4].points,
        'username5': p[5].username,
        'points5' : p[5].points,
        'username6': p[6].username,
        'points6' : p[6].points,
        'username7': p[7].username,
        'points7' : p[7].points,
        'username8': p[8].username,
        'points8' : p[8].points,
        'username9': p[9].username,
        'points9' : p[9].points,
        'curruser':pe.username,
        'currpoint':pe.points,


    }

    return render(request,'users/leaderboard.html',{'dat':t})


