from django.forms import ModelForm

from sceneviewer.models import Scene

class SceneForm(ModelForm):
	class Meta:
		model = Scene
		fields = ["title", "description", "image_file"]