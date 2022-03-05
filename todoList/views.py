from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from todoList.models import Users

user_id = 0

# Create your views here.
def index(request):
    return render(request, "todoList/index.html")

def login(request):
    if request.method == 'GET':
        return render(request, "todoList/login.html")

def register(request):

    """ Register user """

    if request.method == 'GET':
        return render(request, "todoList/register.html")

    if request.method == 'POST':

        # Ensure username was submitted
        if not request.POST["username"]:
            return HttpResponse("Must provide username", 400)

        # Ensure password was submitted
        elif not request.POST["password"]:
            return HttpResponse("Must provide password", 400)

        #Ensure field is not empty
        elif not request.POST["confirmation"]:
            return HttpResponse("Must confirm password", 400)

        #Ensure password is matching
        elif not (request.POST["confirmation"] == request.POST["password"]):
            return HttpResponse("Password is not matching", 400)

        #Ensure there is no duplicate for usename
        existing_user=request.POST["username"]
        password=request.POST["password"]
        old_user = Users.objects.filter(username=existing_user)

        # if the username does not exist in the db, it will be inserted
        if len(old_user) == 0:
            user = Users(user_id, existing_user, password)
            user_id += 1
            user.save()
        else:
            return HttpResponse("User name not available",400)

        return render(request,"todoList/registered.html", user_name=existing_user)



