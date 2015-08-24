"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

# import view functions from trips app
from portal.view import *
from device.views import *
# from storage.views import *
from network.views import *
# from support.views import *
# from account.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^device/$', device, name='device'),
    url(r'^device/device_list/$', device_list, name='device_list'),
    url(r'^device/baremetal_detail/(?P<device_id>\d{1,})/$', device_detail_baremetal),
    url(r'^device/virtual_server_detail/(?P<device_id>\d{1,})/$', device_detail_virtual_server),
    # url(r'^device/', )
    url(r'^network/$', network, name='network'),
    url(r'^network/bandwidth_summary/', bandwidth_summary, name='bandwidth_summary'),
]