from django.shortcuts import render, redirect
#redirect mai ham bss url dete hai
def home(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        upassword = request.POST.get('upassword')
        if uname == 'ok' and upassword == 'ok':
            return redirect('success')
        else:
            return redirect('invalid')
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

def invalid(request):
    return render(request, 'invalid.html')