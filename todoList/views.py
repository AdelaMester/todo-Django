from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "todoList/index.html")

def request_identity(request):
    if request.method == 'GET':
        return render(request, "todoList/login.html")