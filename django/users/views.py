from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .bootstrap_forms import PasswordChangingForm, BackgroundImageForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout
from django.views.generic import DetailView

from .bootstrap_forms import EditProfileForm
from django.contrib import messages

from django.views import generic
from .models import Profile
from userposts.models import Post
from django.contrib.auth.models import User

from .bootstrap_forms import ProfileEditForm

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'users/user_profile.html'
    context_object_name = 'page_user'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])


def profile(request):
    return render(request, 'users/profile.html', {})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): #form validation
            login(request, form.save())
            return redirect("/")  #can be changed later to redirect to home page 
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
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})     

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/') #should be later changed to another page
    
@login_required    
def edit_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangingForm(user=request.user)  # Empty by default
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditProfileForm(instance=request.user)
        password_form = PasswordChangingForm(user=request.user)
    return render(request, 'users/edit_user.html', {
        'form': form,
        'password_form': password_form,
    })

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangingForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  #Prevents logout
            messages.success(request, "Password changed successfully.")
            return redirect('/')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangingForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'users/user_profile.html'
    context_object_name = 'page_user'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView,
             self).get_context_data(*args, **kwargs)
        # add extra fields
        user = User.objects.get(username=self.kwargs['username'])
        context["posts"] = Post.objects.filter(user=user).exclude(title__isnull=True)
        context["replies"] = Post.objects.filter(user=user).exclude(title__isnull=False)
        return context
    
#will use get_context_data() if we want to show users posts etc in user profile 

@login_required
def EditProfileView(request, username):
    
    if request.user.username != username:
        return redirect('/') 

    profile = get_object_or_404(Profile, user__username=username)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_page', username=username)
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def change_background(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = BackgroundImageForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    return redirect('profile_page', username=request.user.username)