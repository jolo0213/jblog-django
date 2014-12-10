from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		('Post Name', {'fields':['title']}),
		('Post Details',{'fields':['pub_date','entry'],'classes':'collapse'}),
	]
	list_display = ('title','pub_date','was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['title']

admin.site.register(Post, PostAdmin)
