from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from vege.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def recepies(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data["receipe_name"]
        receipe_description = data["receipe_description"]
        receipe_image = request.FILES.get("receipe_image")
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        print(request.POST)
        return redirect("/recepies")
    
    queryset = Receipe.objects.all()
    context = { 'recepies': queryset }

    return render(request, "receipes.html", context)

@login_required(login_url="/login/")
def delete_recepies(request, id):
    if request.method == "POST":
        queryset = Receipe.objects.get(id=id)
        queryset.delete()
        print(id)
        
    return redirect("/recepies")

@login_required(login_url="/login/")
def update_recepies(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        ### update
        data = request.POST

        receipe_name = data["receipe_name"]
        receipe_description = data["receipe_description"]
        receipe_image = request.FILES.get("receipe_image")

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect("/recepies")
    
    context = {'recepies': queryset }
        
    return render(request, "receipes-update.html", context)


def login_page(request):
    if request.method == "POST":
        try:
            print("request.post =>>> ", request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            if not User.objects.filter(username = username).exists():
                messages.error(request, "User does not exists!")
                return redirect("/login")
            
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, "User name or password is incorrect!")
                return redirect("/login")
            else:
                login(request, user=user)
                return redirect("/recepies")
            
        except Exception as e:
            messages.error(request, str(e))
            print("Exception =>> \n ", e, '\n')
        return redirect("/login/")
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        try:
            print("request.post =>>> ", request.POST)
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('user_name')
            password = request.POST.get('password')

            if User.objects.filter(username = username).exists():
                print("User already exists")
                messages.error(request, "User already exists")
                return redirect("/register")

            user = User.objects.create(
                email = email,
                first_name = first_name,
                last_name = last_name,
                username = username,
            )

            print("after User object create")
            user.set_password(password)
            user.save()
        except Exception as e:
            print("Exception =>> \n ", e, '\n')
        return redirect("/register/")

    return render(request, "register.html")

@login_required(login_url="/login/")
def logout_user(request):
    try:
        logout(request)
    except Exception as e:
        messages.error(request, "str(e)")
        print("Exception in logout =>> \n ", e, '\n')
        return redirect("/recepies")
    return redirect("/login/")