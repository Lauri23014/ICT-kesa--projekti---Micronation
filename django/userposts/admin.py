from django.contrib import admin
from .models import Post

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	fields = ["id", "replying_to", "text_content", "image_file", "comment_count", "active", "upload_datetime"]
	list_display = ["id", "user", "replying_to", "text_content", "image_file", "comment_count", "active", "upload_datetime"]
	readonly_fields = ["id", "comment_count", "upload_datetime"]
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)