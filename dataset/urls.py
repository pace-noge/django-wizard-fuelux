from django.conf.urls import patterns, include, url
from .views import home, publication

urlpatterns = patterns('',
    url(r'^$', home, name='dataset_index'),
    url(r'^publication/$', publication, name="publication"),
)
