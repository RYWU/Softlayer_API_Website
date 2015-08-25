from django.conf.urls import patterns, include, url
from django.contrib import admin

from Ticket.views import *
from User.views import *
from Billing.views import *
from Portal.view import *
from device.views import *
from network.views import *

urlpatterns = patterns('',

    url(r'^device/$', device, name='device'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^support/$', support, name='support'),
    url(r'^account/$', account, name='account'),
    url(r'^support/ticket/$',ticket,name='ticket'),
    url(r'^account/user/$',user,name='user'),
    url(r'^account/billing/$',billing,name='billing'),
    url(r'^account/user/profile/$',profile,name='profile'),
    url(r'^account/user/399465/$',internpro,name='internpro'),
    url(r'^$',home,name='home'),
    url(r'^device/device_list/$', device_list, name='device_list'),
    url(r'^device/baremetal_detail/(?P<device_id>\d{1,})/$', device_detail_baremetal),
    url(r'^device/virtual_server_detail/(?P<device_id>\d{1,})/$', device_detail_virtual_server),
    url(r'^network/$', network, name='network'),
    url(r'^network/bandwidth_summary/', bandwidth_summary, name='bandwidth_summary'),
)
