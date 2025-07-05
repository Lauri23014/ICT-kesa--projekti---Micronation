from django.http import HttpResponse
from django.shortcuts import render

from userposts.models import Post

# Create your views here.

def post(request, username, post):
	if Post.objects.get(id=post).user.username == username:
		thread = []
		mainpost = Post.objects.get(id=post)
		p = mainpost
		while p.linked_post is not None:
			np = Post.objects.get(id=p.linked_post.id)
			thread.insert(0, np)
			p = np
		comments = Post.objects.filter(linked_post=post)
		context = {
			"username" : username,
			"post" : mainpost,
			"replies" : comments,
			"thread" : thread
		}
		return render(request, "userposts/post_detail_view.html", context=context)
	else:
		# TODO: 404 redirect
		return HttpResponse("teehee")

def postlist(request):
	posts = Post.objects.order_by("-datetime").exclude(title=None)
	context = {
		"posts" : posts
	}
	return render(request, "userposts/post_list_view.html", context=context)

def get_post_date(obj : Post):
	return obj.datetime