from django.shortcuts import render

def user_profile(request, user_id):
    return render(request, "users/profile.html", {"user_id": user_id})
