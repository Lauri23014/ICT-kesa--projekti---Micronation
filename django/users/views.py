from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm

def profile(request):
    return render(request, 'users/profile.html', {})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): #form validation
            form.save()
            return redirect("index")  #can be changed later to redirect to home page 
    else:
        form = UserCreationForm()  

    return render(request, "users/register.html", {"form": form})  
