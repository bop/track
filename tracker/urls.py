from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^ticket/', include('ticket.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
