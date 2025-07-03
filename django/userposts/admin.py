from django.contrib import admin
from .models import Post

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	fields = ["id", "linked_post", "text_content", "image_file", "comment_count", "like_count", "active", "datetime"]
	list_display = ["id", "user", "linked_post", "text_content", "image_file", "comment_count", "like_count", "active", "datetime"]
	readonly_fields = ["id", "comment_count", "like_count", "datetime"]
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)