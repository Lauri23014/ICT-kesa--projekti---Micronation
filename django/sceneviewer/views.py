from django.shortcuts import render


def index(request):
	return render(request, "sceneviewer/marzipano/app-files/index.html")
    #return HttpResponse("Hello, world. You're at the sceneviewer index.")	#simple hello world