from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('invalid/',views.invalid,name='invalid'),
    path('logout/',views.logout,name='logout')
]
