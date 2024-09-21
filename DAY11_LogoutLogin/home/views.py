from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return redirect('invalid')
        else:
            auth.login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')
    
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        # tel = request.POST['tel']
        cp = request.POST['cp']
        if password == cp:
            new_user = User.objects.create(username=username, email=email, password=password)
            # new_user = User.objects.create(username=username, email=email, password=password, tel = tel)
            new_user.set_password(password)
            new_user.save()
            return redirect('dashboard')
        else:
            return redirect('signup')
    return render(request, 'signup.html')

def dashboard(request):
    user = request.user
    parameters = {
        "user":user
    }
    return render(request, 'dashboard.html',parameters)

def logout(request):
    auth.logout(request)
    return redirect('/')

def invalid(request):
    return render(request, 'invalid.html')