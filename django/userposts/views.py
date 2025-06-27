from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post(request, username, post):
	return HttpResponse(username+" - "+post)
	#return render(request, "userposts/post.html")