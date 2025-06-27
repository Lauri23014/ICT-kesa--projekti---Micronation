from django.urls import path

from . import views

urlpatterns = [
    path("<username>/post/<post>", views.post, name="post"),
]