from django.contrib import admin
from .models import Post

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	fields = ["replying_to", "text_content", "image_file", "active", "upload_datetime", "update_datetime"]
	list_display = ["user", "replying_to", "text_content", "image_file", "active", "upload_datetime", "update_datetime"]
	readonly_fields = ["upload_datetime", "update_datetime"]
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)