from django.shortcuts import render

def index(request):
    return render(request, 'reunion/index.html')

def detail(request):
    return render(request, 'reunion/detail.html')