from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home,name='home'),
    # path('login/',views.login,name='login'),
    # path('success/',views.success,name='success')
    path('',views.ok,name='ok')
]
