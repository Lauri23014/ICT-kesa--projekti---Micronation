from django.urls import path

from . import views

urlpatterns = [
    path("profile/<username>/post/<post>", views.post),
	path("timeline", views.postlist)
]