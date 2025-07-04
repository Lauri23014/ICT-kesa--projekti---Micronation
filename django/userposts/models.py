from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# TODO: retain/archive post/comment content on deletion?

# TODO: add likes(?)
# TODO: fields for storing amount of likes(?)

def user_directory_path(instance, filename):
	# file will be uploaded to MEDIA_ROOT/posts/username/<filename>
	return "posts/{0}/{1}".format(instance.user.username, filename)

def image_attached(self):
		if self.image_file:
			return " [image attached]"
		return ""

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	linked_post = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=127)
	text_content = models.TextField(blank=True, null=True, max_length=255)
	datetime = models.DateTimeField(auto_now_add=True)
	image_file = models.ImageField(blank=True, null=True, upload_to=user_directory_path) # maybe add django-cleanup to project to clean unused user files?
	active = models.BooleanField(default=False) # only active posts should be visible on site, posts default to inactive and are either automatically approved or checked by admin
	@property
	def comment_count(self):
		return len(Post.objects.filter(linked_post=self.id))
	@property
	def like_count(self):
		return len(Like.objects.filter(linked_post=self.id))
	def __str__(self):
		return self.user.username+": "+self.text_content+image_attached(self)
	def clean(self):
		if self.linked_post and self.title:
			raise ValidationError({'title': 'Comments cannot have titles'})
		if not self.text_content and not self.image_file:  # This will check for None or Empty
			raise ValidationError({'text_content': 'One of text_content or image_file should be filled.'})
		
class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	linked_post = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
	datetime = models.DateTimeField(auto_now_add=True)