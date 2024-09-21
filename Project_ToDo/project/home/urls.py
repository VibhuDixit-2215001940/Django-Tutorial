from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('invalid/',views.invalid,name='invalid'),
    path('todo/',views.todo,name='todo'),
    path('logout/',views.logout,name='logout'),
]
