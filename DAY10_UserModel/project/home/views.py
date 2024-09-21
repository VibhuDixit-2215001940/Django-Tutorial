from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin':
            return redirect('dashboard')
        else:
            return redirect('invalid')
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
    return render(request, 'dashboard.html')

def invalid(request):
    return render(request, 'invalid.html')