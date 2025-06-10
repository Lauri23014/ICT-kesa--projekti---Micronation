from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SceneForm


def index(request):
	return render(request, "sceneviewer/index.html")
	#return render(request, "sceneviewer/marzipano/app-files/index.html")
    #return HttpResponse("Hello, world. You're at the sceneviewer index.")	#simple hello world

def upload_scene(request):
	# if this is a POST request we need to process the form data
	if request.method == "POST":
		# create a form instance and populate it with data from the request:
		form = SceneForm(request.POST, request.FILES)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			form.save()
			return HttpResponseRedirect("/view")

	# if a GET (or any other method) we'll create a blank form
	else:
		form = SceneForm()
	return render(request, "sceneviewer/upload_scene.html", {"form": form})