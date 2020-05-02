from django.urls import path,include
from . import views
from users import views as user_view

urlpatterns = [
    path('', views.home,name='mysite-home'),
    #path('register/',user_view.register,name='register')

]
