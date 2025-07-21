from copy import copy
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from userposts.models import Post
from sceneviewer.models import Scene

from sceneviewer.views import scene_view

from zoneinfo import ZoneInfo

# basic views
def post_detail_view(request, username, id):
	if Post.objects.get(id=id).user.username == username:
		thread = []
		mainpost = Post.objects.get(id=id)
		p = mainpost
		while p.linked_post is not None or p.linked_scene is not None:
			np = None
			if p.linked_post is not None:
				np = Post.objects.get(id=p.linked_post.id)
				thread.insert(0, np)
				p = np
			else:
				np = Scene.objects.get(id=p.linked_scene.id)
				thread.insert(0, np)
				break
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

# view for adding or removing likes
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

# views for making posts and comments
def create_post(request, linked_post=None, linked_scene=None, title=None, text_content=None, image_file=None):
	data = {}

	post = Post(user=request.user, linked_post=linked_post, linked_scene=linked_scene, title=title, text_content=text_content, image_file=image_file)

	success = True
	id = 0
	username = ""
	try:
		post.save()
		id = post.id
		username = post.user.username
	except:
		print("no post created")
		success = False

	data["success"] = success
	data["username"] = username
	data["id"] = id

	return JsonResponse(data)

def post_post(request, username, id):
	title = request.POST.get("post_title")
	text_content = request.POST.get("post_text")
	return create_post(request, title=title, text_content=text_content)

def comment_post(request, username, id):
	linked_post = Post.objects.get(id=id)
	text_content = request.POST.get("comment_text")
	return create_post(request, linked_post=linked_post, text_content=text_content)

def comment_scene(request, id): 
	linked_scene = Scene.objects.get(id=id)
	text_content = request.POST.get("comment_text")
	return create_post(request, linked_scene=linked_scene, text_content=text_content)

def remove_post(request, username, id):
	post = Post.objects.get(id=id)

	if post is None:
		data = {}
		data["success"] = False
		return JsonResponse(data)
	elif post.user.id is request.user.id:
		if post.linked_post:
			next_id = copy(post.linked_post.id)
			next_username = copy(post.linked_post.user.username)
			post.delete()
			return redirect("post_detailed_view", username=next_username, id=next_id)
		elif post.linked_scene:
			next_id = copy(post.linked_scene.id)
			post.delete()
			return redirect("scene", id=next_id)
		else:
			post.delete()
			return redirect("list_of_posts")

def convert_post_timezone(request, username, id):
	data = {}
	post = Post.objects.get(id=id)
	data["datetime_string"] = post.datetime.astimezone(ZoneInfo(request.POST.get("timezone"))).strftime("%d/%m/%Y, %H:%M:%S")
	return JsonResponse(data)