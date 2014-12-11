import json

from datetime import datetime

from django.shortcuts import render, get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

from blog.models import Post

def index(request):
	posts = Post.objects.all().order_by('-pub_date')
	return render(request,'blog/index.html',{'posts':posts,})