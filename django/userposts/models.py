from django.db import models
from django.db.models import Q
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
	title = models.CharField(blank=True, null=True, max_length=127)
	text_content = models.TextField(blank=True, null=True, max_length=255)
	datetime = models.DateTimeField(auto_now_add=True)
	image_file = models.ImageField(blank=True, null=True, upload_to=user_directory_path) # maybe add django-cleanup to project to clean unused user files?
	likes = models.ManyToManyField(User, blank=True, default=None, related_name="likes")
	active = models.BooleanField(default=False) # only active posts should be visible on site, posts default to inactive and are either automatically approved or checked by admin
	@property
	def comment_count(self):
		count = 0
		comments = Post.objects.filter(linked_post=self.id)
		count += comments.count()
		for comment in comments:
			count +=comment.comment_count
		return count
	@property
	def like_count(self):
		return self.likes.count()
	def __str__(self):
		return self.user.username+": "+self.text_content+image_attached(self)
	
	class Meta:
		constraints = [
			models.CheckConstraint(condition=Q(title__isnull=True) ^ Q(linked_post__isnull=True), name="post-title-constraint"),
			models.CheckConstraint(condition=Q(text_content__isnull=False) | Q(image_file__isnull=False), name="post-content-constraint"),
		]