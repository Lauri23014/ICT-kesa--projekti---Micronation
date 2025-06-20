from django.contrib import admin
from .models import Post, Comment

# Register your models here.

#TODO: make proper admin views
admin.site.register(Post)
admin.site.register(Comment)