from django.shortcuts import render


def index(request):
    return render(request, 'user/index.html')

def login(request):
    return render(request, 'user/login.html')