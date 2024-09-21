from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mera_pannel/', admin.site.urls),
    path('',include('home.urls'))
]
