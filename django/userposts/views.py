from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from userposts.models import Post

# Create your views here.

def post(request, username, id):
	if Post.objects.get(id=id).user.username == username:
		thread = []
		mainpost = Post.objects.get(id=id)
		p = mainpost
		while p.linked_post is not None:
			np = Post.objects.get(id=p.linked_post.id)
			thread.insert(0, np)
			p = np
		comments = Post.objects.filter(linked_post=id)
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

def add_or_remove_like(request, username, id):
	data = {}

	post = Post.objects.get(id=id)
	print(id)

	if request.method == "POST":
		user = request.user
		if post.likes.filter(id=user.id).exists():
			liked = False
			post.likes.remove(user)
		else:
			post.likes.add(user)
			liked = True


	data["count"] = post.likes.count()
	data["liked"] = liked
	return JsonResponse(data) 