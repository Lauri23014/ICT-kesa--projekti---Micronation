from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
	path("upload", views.upload_scene, name="upload")
]