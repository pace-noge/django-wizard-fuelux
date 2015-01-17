from django.conf.urls import patterns, include, url
from django.contrib import admin
import dataset

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wizard.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dataset/', include('dataset.urls')),
)
