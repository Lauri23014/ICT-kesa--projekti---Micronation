from django.http import HttpResponse
from django.shortcuts import render

from userposts.models import Post

# Create your views here.


# TODO: page for posts
# django tutorial for templates (look "include")
# | https://docs.djangoproject.com/en/5.2/ref/templates/builtins/
# format:
# (post-mini1) 	op
# (post-mini2) 	replying to op
# post			replying to post-mini2
# (post-mini3) 	reply to post
def post(request, username, post):
	if Post.objects.get(id=post).user.username == username:
		thread = []
		p = Post.objects.get(id=post)
		while p.replying_to is not None:
			np = Post.objects.get(id=p)
			thread.insert(0, np)
			p = np.replying_to
		context = {
			"username" : username,
			"post" : Post.objects.get(id=post),
			"replies" : Post.objects.filter(replying_to=post),
			"thread" : thread
		}
		return render(request, "userposts/post.html", context=context)
	else:
		# TODO: 404 redirect
		return HttpResponse("teehee")