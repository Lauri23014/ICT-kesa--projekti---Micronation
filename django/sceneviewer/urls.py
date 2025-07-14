from django.urls import path

from . import views

urlpatterns = [
	path("<id>", views.scene_view, name="scene"),
]