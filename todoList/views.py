from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "todoList/index.html")

def login(request):
    if request.method == 'GET':
        return render(request, "todoList/login.html")