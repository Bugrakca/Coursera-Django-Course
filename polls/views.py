from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. You are at the polls index.")

def home_screen(request):
    print('-----'*20, '\n', request.headers)
    print('-----'*20, '\n', request)
    return render(request, 'static/home.html', {})