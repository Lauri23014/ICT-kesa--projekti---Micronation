"""
URL configuration for micronation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve


urlpatterns = [
	path("view/", include("sceneviewer.urls")),
    path("admin/", admin.site.urls),
    path("", include("map.urls")),
    path("profile/", include("users.urls")),
    path("", include("userposts.urls")),
    path("about_us/", include("about.urls"))
]

# Serves media files if in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),]