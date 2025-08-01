from django.contrib import admin
from .models import Scene

# Register your models here.

#admin.site.register(Scene)
@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
	fields = ["id", "title", "description", "image_file", "thumbnail", "is_360", "latitude", "longitude", "upload_datetime", "update_datetime"]
	list_display = ["id", "title", "description", "image_file", "thumbnail", "is_360", "latitude", "longitude", "upload_datetime", "update_datetime"]
	readonly_fields = ["id", "upload_datetime", "update_datetime"]