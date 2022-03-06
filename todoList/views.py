from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import connection
from todoList.models import Users
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session
from django.shortcuts import redirect

user_id = 0

# Create your views here.
def index(request):
    return render(request, "todoList/index.html")

def login(request):
    # Forget any user_id
    # session.clear()

    if request.method == 'GET':
        return render(request, "todoList/login.html")

    if request.method == 'POST':
        # Ensure username was submitted
        if not request.POST["username"]:
            return HttpResponse("must provide username", 403)

        # Ensure password was submitted
        elif not request.POST["password"]:
            return HttpResponse("must provide password", 403)

        # Query database for username
        #with connection.cursor() as cursor:
        #    users = cursor.execute("SELECT * from todoList_users WHERE username = %s", [request.POST["username"]])
        users = Users.objects.get(username=request.POST["username"])
        print(users)

        # Ensure username exists and password is correct
        # if len(rows) != 1 -> as in to check there is only one user with that username
        #if the hashse are not equal, that means the password is not correct for that user
        if not check_password(request.POST["password"],users.hash_password):
            return HttpResponse("Invalid username and/or password", 403)

        # Remember which user has logged in
        request.session["user_id"] = users.user_id
        print(request.session["user_id"])

        # Redirect user to home page
        return redirect("/")

        #rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        #with connection.cursor() as cursor:
        #        cursor.execute("INSERT INTO todoList_users (username, hash_password) VALUES (%s, %s)", [existing_user, make_password(password)])
        #else:


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
        global user_id
        if len(old_user) == 0:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO todoList_users (username, hash_password) VALUES (%s, %s)", [existing_user, make_password(password)])
        else:
            return HttpResponse("User name not available",400)

        return render(request,"todoList/registered.html", {
            "user_name": existing_user
        })


def logout(request):
    # Forget any user_id
    print(request.session["user_id"])
    request.session.clear()

    if request.method == 'GET':
        return render(request, "todoList/login.html")


