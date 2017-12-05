
from django.conf.urls import url, include, patterns

from views import index, submission

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^submit$', submission),
)
