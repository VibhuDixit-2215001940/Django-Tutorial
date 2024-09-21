from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def help(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        print(uname)
        print(uemail)
    return render(request, 'help.html')