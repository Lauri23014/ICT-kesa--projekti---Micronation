from copy import copy
from datetime import datetime, timezone
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import redirect, render

from userposts.models import Post
from sceneviewer.models import Scene

from zoneinfo import ZoneInfo

from  django.core.files.images import ImageFile

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

		comments = sorted(Post.objects.filter(linked_post=id), key=get_post_like_count, reverse=True)
		context = {
			"username" : username,
			"post" : mainpost,
			"replies" : comments,
			"thread" : thread
		}
		return render(request, "userposts/post_detail_view.html", context=context)
	else:
		raise Http404("Post could not be found.")
	
def get_post_like_count(post : Post):
	return post.like_count

def postlist(request):
	# posts = sorted(Post.objects.exclude(title=None), key=get_post_popularity, reverse=True)
	posts = Post.objects.exclude(title=None).order_by("-datetime")
	context = {
		"posts" : posts
	}
	return render(request, "userposts/post_list_view.html", context=context)

def get_post_date(post : Post):
	return post.datetime

def get_post_popularity(post : Post):
	time_since = datetime.now(timezone.utc) - get_post_date(post)
	return get_post_like_count(post) / (time_since.total_seconds() * 24*60*60) # like count / days since post was made

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

	if image_file is not None:
		image_file = ImageFile(image_file)

	post = Post(user=request.user, linked_post=linked_post, linked_scene=linked_scene, title=title, text_content=text_content, image_file=image_file)

	success = True
	id = 0
	username = ""
	try:
		post.clean()
		post.save()
		id = post.id
		username = post.user.username
	except Exception as e:
		success = False

	data["success"] = success
	data["username"] = username
	data["id"] = id

	return JsonResponse(data)

def post_post(request):
	title = request.POST.get("post_title")
	text_content = request.POST.get("post_text")
	image_file = image_file_or_none(request.FILES)
	return create_post(request, title=title, text_content=text_content, image_file=image_file)

def comment_post(request, username, id):
	linked_post = Post.objects.get(id=id)
	text_content = request.POST.get("comment_text")
	image_file = image_file_or_none(request.FILES)
	return create_post(request, linked_post=linked_post, text_content=text_content, image_file=image_file)

def comment_scene(request, id): 
	linked_scene = Scene.objects.get(id=id)
	text_content = request.POST.get("comment_text")
	image_file = image_file_or_none(request.FILES)
	return create_post(request, linked_scene=linked_scene, text_content=text_content, image_file=image_file)

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
			return redirect("timeline")

def convert_post_timezone(request, username, id):
	data = {}
	post = Post.objects.get(id=id)
	data["datetime_string"] = post.datetime.astimezone(ZoneInfo(request.POST.get("timezone"))).strftime("%d/%m/%Y, %H:%M:%S")
	return JsonResponse(data)

def image_file_or_none(request_files):
	if request_files:
		return ImageFile(request_files["image_file"])
	else:
		return None