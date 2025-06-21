from django.contrib import admin
from .models import Post, Comment

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	fields = ["title", "text_content", "image_file", "active", "upload_datetime", "update_datetime"]
	list_display = ["user", "title", "text_content", "image_file", "active", "upload_datetime", "update_datetime"]
	readonly_fields = ["upload_datetime", "update_datetime"]
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)

#admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	fields = ["post", "text_content", "active", "upload_datetime", "update_datetime"]
	list_display = ["user", "post", "text_content", "active", "upload_datetime", "update_datetime"]
	readonly_fields = ["upload_datetime", "update_datetime"]
	def post_title(self, obj):
		return obj.post.title
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)