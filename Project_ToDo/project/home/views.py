from django.contrib.auth.decorators import login_required  # Import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from . models import Todo
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('todo')
        else:
            return redirect('invalid')
    return render(request, 'login.html')

def invalid(request):
    return render(request, 'invalid.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cp = request.POST['cp']
        if password == cp:
            new_user = User.objects.create(username=username, email=email, password=password)
            new_user.set_password(password)
            new_user.save()
            return redirect('todo')
        else:
            return redirect('signup')
    return render(request, 'signup.html')

@login_required(login_url='login')
def todo(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()  # Get 'name' or default to empty string
        desc = request.POST.get('desc', '').strip()  # Get 'desc' or default to empty string
        
        # Validate form data
        if not name:
            return HttpResponse("Name is required.", status=400)
        if not desc:
            return HttpResponse("Description is required.", status=400)

        new_todo = Todo.objects.create(name=name,desc=desc)
        new_todo.save()
    return render(request, 'todo.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')