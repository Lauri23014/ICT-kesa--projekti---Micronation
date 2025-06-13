from django.contrib import admin
from .models import Scene

# Register your models here.

#admin.site.register(Scene)
@admin.register(Scene)
class SceneAdmin(admin.ModelAdmin):
	list_display = ["title", "description", "image_file", "upload_datetime", "update_datetime"]
	readonly_fields = ["upload_datetime", "update_datetime"]