from django.conf.urls import patterns, include, url
from .views import home, publication, article, article_property

urlpatterns = patterns('',
    url(r'^$', home, name='dataset_index'),
    url(r'^publication/$', publication, name="publication"),
    url(r'^article/$', article, name="article"),
    url(r'^property/$', article_property, name="article_property"),
)
