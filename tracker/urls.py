from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from ticket.databrowse_config import *

urlpatterns = patterns('',
    url(r'^ticket/', include('ticket.urls')),
    url(r'^databrowse/(.*)', databrowse.site.root),

    url(r'^admin/', include(admin.site.urls)),
)
