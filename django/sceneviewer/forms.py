from django.forms import ModelForm

from sceneviewer.models import Scene

class SceneForm(ModelForm):
	class Meta:
		model = Scene
		fields = ["text_file", "image_file"]