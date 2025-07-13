from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Scene
from userposts.models import Post

def index(request):
	return render(request, "sceneviewer/index.html")

def scene_view(request, id):
	scene = Scene.objects.get(id=id)
	comments = Post.objects.filter(linked_scene=scene)
	context = {
		"scene" : scene,
		"comments" : comments
	}
	return render(request, "sceneviewer/scene_view.html", context=context)