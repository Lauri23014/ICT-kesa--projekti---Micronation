from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("profile/<username>/post/<id>", views.post_detail_view, name="post_detailed_view"),
	path("profile/post", login_required(views.post_post), name="create_post"),
	path("profile/<username>/post/<id>/remove", login_required(views.remove_post), name="remove_post_or_comment"),
	path("profile/<username>/post/<id>/like", login_required(views.add_or_remove_like), name="add_or_remove_like"),
	path("profile/<username>/post/<id>/comment", login_required(views.comment_post), name="comment_post"),
	path("profile/<username>/post/<id>/timezone", views.convert_post_timezone, name="convert_post_timezone"),
	path("view/<id>/comment", login_required(views.comment_scene), name="comment_scene"),
	path("timeline", views.postlist, name="timeline")
]