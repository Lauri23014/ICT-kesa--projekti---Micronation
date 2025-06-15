from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def profile(request):
    return render(request, 'users/profile.html', {})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): #form validation
            login(request, form.save())
            return redirect("index")  #can be changed later to redirect to home page 
    else:
        form = UserCreationForm()  

    return render(request, "users/register.html", {"form": form})  

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("index")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})     

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("index") #should be later changed to another page