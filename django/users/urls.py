from django.urls import path
from . import views



urlpatterns = [
    path("", views.profile, name="profile"),
    path('register/', views.register_view, name ="register")
]
