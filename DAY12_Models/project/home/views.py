from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required  # Import login_required
from django.contrib import auth
def index(request):
    return render(request, 'index.html')

def invalid(request):
    return render(request, 'invalid.html')

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    parameters = {
        "user":user
    }
    return render(request, 'dashboard.html',parameters)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        new_user = auth.authenticate(username=username, password=password)
        if new_user is None:
            return redirect('invalid')
        else:
            auth.login(request, new_user)
            return redirect('dashboard')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cp = request.POST['cp']
        if password == cp:
            new_user = User.objects.create(username=username, email=email, password=password)
            new_user.set_password(password)
            new_user.save()
            return redirect('dashboard')
        else:
            return redirect('signup')
    return render(request, 'signup.html')
    
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')