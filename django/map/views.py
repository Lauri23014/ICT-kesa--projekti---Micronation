from django.shortcuts import render
from sceneviewer.models import Scene

# Create your views here.
def index(request):
	context = {
		"scenes" : Scene.objects.all()
	}
	return render(request, "map/index.html", context=context)
