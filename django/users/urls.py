from django.urls import path
from . import views
from .views import ProfilePageView, EditProfileView
from django.contrib.auth import views as auth_views



urlpatterns = [
    
    path('register/', views.register_view, name ="register"),
    path('login/', views.login_view, name ="login"),
    path('logout/', views.logout_view, name ="logout"),
    path('edit/', views.edit_view, name ="edit"),
    path('password/', views.password_change, name="password_change"),
    path('<str:username>/profile/', ProfilePageView.as_view(), name='profile_page'),
    path('<str:username>/edit_profile/', EditProfileView, name='edit_profile'),
    path('change_background/', views.change_background, name='change_background'),
    
    
    
]
