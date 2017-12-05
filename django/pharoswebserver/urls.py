from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pharoswebserver.views.home', name='home'),
    url(r'^', include('frontend.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
