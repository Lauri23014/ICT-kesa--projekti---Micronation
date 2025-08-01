from django.db import models

# unused
def user_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/scenes/<filename>
	return "scenes/images/{0}".format(filename)

def image_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/scenes/<filename>
	return "scenes/images/{0}".format(filename)

def thumbnail_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/scenes/<filename>
	return "scenes/thumbnails/{0}".format(filename)

class Scene(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	upload_datetime = models.DateTimeField(auto_now_add=True)
	update_datetime = models.DateTimeField(auto_now=True)
	image_file = models.ImageField(upload_to=image_directory_path)
	thumbnail = models.ImageField(upload_to=thumbnail_directory_path)
	is_360 = models.BooleanField()
	latitude = models.FloatField(default=60.73958103204708)
	longitude = models.FloatField(default=24.75605680821921)
	def __str__(self):
		return self.title