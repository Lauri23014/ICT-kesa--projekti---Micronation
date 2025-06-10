from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/scenes/<filename>
    return "scenes/{0}".format(filename)

class Scene(models.Model):
	text_file = models.FileField(upload_to=user_directory_path)
	image_file = models.ImageField(upload_to=user_directory_path)