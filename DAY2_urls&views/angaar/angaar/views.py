from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World! This is the index page of the Agaar application.")