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

    """ Login user """


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
        users = Users.objects.get(username=request.POST["username"])
        print(users)

        # Ensure username exists and password is correct
        # If the hashse are not equal, that means the password is not correct for that user
        if not check_password(request.POST["password"],users.hash_password):
            return HttpResponse("Invalid username and/or password", 403)

        # Remember which user has logged in
        request.session["user_id"] = users.user_id
        print(request.session["user_id"])

        # Redirect user to home page
        return redirect("/")



def register(request):

    """ Register user """

    if request.method == 'GET':
        return render(request, "todoList/register.html")

    if request.method == 'POST':

        # Ensure username was submitted
        if not request.POST.get("username"):
            return HttpResponse("Must provide username", 400)

        # Ensure password was submitted
        elif not request.POST.get("password"):
            return HttpResponse("Must provide password", 400)

        #Ensure field is not empty
        elif not request.POST.get("confirmation"):
            return HttpResponse("Must confirm password", 400)

        #Ensure password is matching
        elif not (request.POST.get("confirmation") == request.POST.get("password")):
            return HttpResponse("Password is not matching", 400)

        #Ensure there is no duplicate for usename
        existing_user=request.POST.get("username")
        password=request.POST.get("password")
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

    """ Logout user """


    # Forget any user_id
    print(request.session["user_id"])
    request.session.clear()

    if request.method == 'GET':
        return render(request, "todoList/login.html")

def tasks(request):

    """ Create tasks """

    # Render the tasks template
    if request.method == 'GET':
        # Query the database to display all tasks
        with connection.cursor() as cursor:
            display_tasks = cursor.execute("SELECT * FROM todoList_tasks WHERE completed='False' AND user_id = (%s)", [request.session["user_id"]]).fetchall()

        return render(request, "todoList/tasks.html", {
            "display_tasks": display_tasks
        })


    # Query database to update tasks table
    if request.method == 'POST':
        # when the task is added in the form it is saved in the 'description' variable
        description = request.POST["task"]
        # Insert into database the new task
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO todoList_tasks (description, completed, user_id) VALUES (%s, %s, %s)", [description, 'False', request.session["user_id"]])
        return HttpResponseRedirect("/tasks")

def update_task(request):

    # update task_id in the database as completed
    if request.method == 'GET':
        read_id = request.GET.get('id')
        with connection.cursor() as cursor:
            cursor.execute("UPDATE todoList_tasks SET completed = (%s) WHERE task_id = (%s) AND user_id = (%s)", ["True", read_id, request.session["user_id"]])

        return HttpResponse("Updated task")


