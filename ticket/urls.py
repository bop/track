from django.conf.urls.defaults import patterns, url
from views import home, ticket_listing

urlpatterns = patterns('',
                       url(r'^home/$', home, name = "home"),
                       url(r'^home/(\w+)$', home, name = "home"),
                       url(r'^$', ticket_listing, name="listing")

)
