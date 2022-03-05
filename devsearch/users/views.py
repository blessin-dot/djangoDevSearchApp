from django.http.response import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'users/index.html')

def users(request):
    return HttpResponse('this is are the users')