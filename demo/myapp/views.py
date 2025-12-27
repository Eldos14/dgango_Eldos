from django.shortcuts import render,HttpResponse
from .models import ToDoItem
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from .models import Course

def home (request):
    courses = Course.objects.all()
    return render (request,'home.html', {'courses': courses})

def todos (request):
    items = ToDoItem.objects.all()
    return render (request,'todos.html', {'todos': items})

def login_view(request):

    return render(request, 'login.html')

def course_page(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_page.html', {'course': course})


def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

     
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )


        login(request, user)

        return redirect('home')  
        
    return render(request, "signup.html")

def logout_view(request):
    return render(request,"signup.html")


def html_page(request):
    return render(request, 'html_page.html')

def css_page(request):
    return render(request, 'css_page.html')

def js_page(request):
    return render(request, 'js_page.html')

def python_page(request):
    return render(request, 'python_page.html')


def test_python(request):
    result = None
    score = 0

    if request.method == "POST":
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")

        if q1 == "5":
            score += 1
        if q2 == "b":
            score += 1

        result = f"Ваш результат: {score} из 2"

    return render(request, "test_python.html", {
        "result": result
    })

