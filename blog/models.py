import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
	title = models.CharField('Title',max_length=200)
	pub_date = models.DateTimeField('Date Published')
	entry = models.TextField(max_length=10000)

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)
	was_published_recently.short_description = 'Published recently (within last week)?'

	def __unicode__(self):
		return self.title