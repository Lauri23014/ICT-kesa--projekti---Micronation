from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# TODO: page for posts
# django tutorial for templates (look "include")
# | https://docs.djangoproject.com/en/5.2/ref/templates/builtins/
# format:
# (post-mini1) 	op
# (post-mini2) 	replying to op
# post			replying to post-mini2
# (post-mini3) 	reply to post
def post(request, username, post):
	return HttpResponse(username+" - "+post)
	#return render(request, "userposts/post.html")