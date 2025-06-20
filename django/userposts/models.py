from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/posts/username/<filename>
	return "posts/{0}/{1}".format(instance.user.username, filename)

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	text_content = models.TextField(blank=True)
	upload_datetime = models.DateTimeField(auto_now_add=True)
	update_datetime = models.DateTimeField(auto_now=True)
	image_file = models.ImageField(blank=True, null=True, upload_to=user_directory_path) #maybe add django-cleanup to project to clean unused user files?
	def __str__(self):
		return self.user.username+": "+self.title
	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text_content = models.TextField()
	upload_datetime = models.DateTimeField(auto_now_add=True)
	update_datetime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.user.username+": "+self.text_content+" ("+self.post.__str__()+")"