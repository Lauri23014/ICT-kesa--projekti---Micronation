from django.http import HttpResponse
from django.shortcuts import render

from userposts.models import Post

# Create your views here.

def post(request, username, post):
	if Post.objects.get(id=post).user.username == username:
		thread = []
		mainpost = Post.objects.get(id=post)
		p = mainpost
		while p.replying_to is not None:
			np = Post.objects.get(id=p.replying_to.id)
			thread.insert(0, np)
			p = np
		comments = Post.objects.filter(replying_to=post)
		context = {
			"username" : username,
			"post" : mainpost,
			"replies" : comments,
			"thread" : thread
		}
		return render(request, "userposts/post.html", context=context)
	else:
		# TODO: 404 redirect
		return HttpResponse("teehee")

def postlist(request):
	posts = Post.objects.order_by("-upload_datetime").all()
	context = {
		"posts" : posts
	}
	return render(request, "userposts/post_list.html", context=context)

def get_post_date(obj : Post):
	return obj.upload_datetime