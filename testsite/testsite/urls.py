from django.conf.urls import patterns, include, url
from django.contrib import admin
from stream.views import Index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^stream/', Index.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
