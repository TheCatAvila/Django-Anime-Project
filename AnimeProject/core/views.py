from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def signup(request):
    return render(request, 'core/auth/signup.html')

def login(request):
    return render(request, 'core/auth/login.html')