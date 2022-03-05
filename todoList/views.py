from django.shortcuts import render
from django.http import HttpResponse
import request

# Create your views here.
def index(request):
    return render(request, "todoList/index.html")

def home(request):
    if request.method == 'GET':

        # Login validation, if there is no session['name'] redirect to / route
        if 'name' not in request.session:
            return HttpResponseRedirect("/")
        return render(request, "todoList/home.html",{
            'name': request.session['name']

        })