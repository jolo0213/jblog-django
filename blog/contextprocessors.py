import json

from blog.models import Post

def newest(request):
	newest = Post.objects.latest('pub_date')
	return { 'newest':newest }
	