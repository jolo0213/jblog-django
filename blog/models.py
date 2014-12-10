from django.db import models

class Post(models.Model):
	title = models.CharField('Title',max_length=200)
	pub_date = models.DateTimeField('Date Published')
	