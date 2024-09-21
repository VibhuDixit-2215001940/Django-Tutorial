from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('invalid/',views.invalid,name='invalid'),
    path('success/',views.success,name='success')
]
