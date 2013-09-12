from django.conf.urls.defaults import patterns, url
from views import home, ticket_listing, ticket_detail, ticket_list

urlpatterns = patterns('',
                       url(r'^home/$', home, name = "home"),
                       url(r'^home/(\w+)$', home, name = "home"),
                       url(r'^$', ticket_listing, name="listing"),
                       url(r'^detail/(\d+)', ticket_detail, name='detail'),
                       url(r'^list/$', ticket_list, name='list')

)
