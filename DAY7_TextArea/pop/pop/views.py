from django.shortcuts import render

# def home(request):
#     return render(request, 'index.html')

# def login(request):
#     if request.method == 'POST':
#         uname = request.POST['uname']
#         upassword = request.POST['upassword']
#         if uname == 'Vibhu' and upassword == 'ok':
#             return render(request, 'success.html')
#     return render(request, 'login.html')

# def success(request):
#     return render(request, 'success.html')

def ok(request):
    if request.method == 'POST':
        mytext = request.POST['mytext']
        if mytext == 'angaar':
            return render(request, 'success.html')
        else:
            return render(request, 'invalid.html')
    return render(request, 'ok.html')