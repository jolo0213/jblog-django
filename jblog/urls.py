from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls',namespace='blog')),
    url(r'^pages/',include('django.contrib.flatpages.urls')),
)
