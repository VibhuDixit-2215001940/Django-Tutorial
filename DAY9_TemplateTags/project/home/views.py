from django.shortcuts import render, redirect

def home(request):
    parameters = {}  # Initialize 'parameters' outside the if block

    if request.method == 'POST':
        username = request.POST.get('username')
        upassword = request.POST.get('upassword')
        parameters = {
            'username': username,
            'upassword': upassword
        }
    return render(request, 'home.html', parameters)

def one(request):
    return render(request, 'one.html')

def two(request):
    return render(request, 'two.html')
