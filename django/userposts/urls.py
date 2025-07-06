from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("profile/<username>/post/<id>", views.post, name="post_detailed_view"),
	path("profile/<username>/post/<id>/like", login_required(views.add_or_remove_like), name="add_or_remove_like"),
	path("timeline", views.postlist, name="list_of_posts")
]