from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('one',views.one,name='one'),
    path('two',views.two,name='two')
]
