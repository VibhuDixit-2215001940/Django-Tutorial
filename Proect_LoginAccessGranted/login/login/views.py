from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        upassword = request.POST['upassword']
        if uname == 'Vibhu' and upassword == 'ok':
            print('Access Granted')
        else :
            print('Access Denied')            
    return render(request, 'login.html')