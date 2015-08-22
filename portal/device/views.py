# device/views.py
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.conf import settings

import json
import markdown2 # Document markup usage. #
import SoftLayer
import requests

SERVICENAME = 'SoftLayer_Account';
METHODNAME = 'getHardware';

class APIHandler:
    """ Create, Revisit, Update, Delete API Users """
    def __init__(self, username=settings.SL_USERNAME,
                 apikey=settings.SL_APIKEY,
                 serviceName=None, methodName=None, mask=None):
        assert serviceName
        assert methodName

        self.username = username;
        self.apikey = apikey;
        self.serviceName = serviceName;
        self.methodName = methodName;
        self.mask = mask;

    def printInfo():
        print ("Username: " + self.username);
        print ("ApiKey: " + self.apikey);
    def functionHandler(self):
        opts = {}
        requestURL = 'https://'+self.username+':'+self.apikey+'@api.softlayer.com/rest/v3/'+ self.serviceName +'/'+ self.methodName +'.json';

        if self.mask:
            opts['objectMask'] = self.mask

        s = requests.Session();
        response = s.get(requestURL, params=opts);
        return response.text;  # return API call html.  
        # return '{}'

# ------------- Utility Functions Starts ----------- #
from device.utils import *
# ------------- Utility Functions Ends----------- #

# ------------- URL-Handler Functions Starts----------- #
def device(request):
    return render(request, ['api_and_function.html'])

def device_list(request):
    return render(request, 
                  ['api_and_function.html'], 
                  {
                   # 'debug': debug_area(),
                   'total_devices_number': count_device(),
                   'baremetal': list_baremetal(),
                   'hourlyvirtualserver': list_hourly_virtual_server(),
                   'monthlyvirtualserver': list_monthly_virtual_server(),
                   # 'api_list': api_list(),
                   'api_doc_md': api_doc_md('device/device_list.md'), 
                  },
                )

def device_detail_baremetal(request, device_id):
    return render(request, 
                  ['api_and_function.html'], 
                  {
                   # 'debug': debug_area(device_id),
                   'device_info': get_device_info_by_id_baremetal(device_id),  
                   'start_date': get_start_date(device_id),
                   'device_type': "Bare Metal",
                   'os': get_os_baremetal(device_id),
                   'ram': get_ram_baremetal(device_id),
                   'processor': get_processors(device_id),
                   'motherboard': get_motherboard(device_id), 
                   'powersupply': get_power_supply(device_id),
                   'drivecontroller': get_drive_controller(device_id),
                   'baremetal_credential': get_baremetal_credential(device_id),
                   'ip_address_baremetal': get_ip_address_baremetal(device_id),
                   'default_dateway_baremetal': get_default_gateway_baremetal(device_id),
                   'subnet_mask_baremetal': get_subnet_mask_baremetal(device_id),
                   'network_interface': get_network_interface(device_id),
                   'api_doc_md': api_doc_md('device/device_detail_baremetal.md'),
                  },
                )

def device_detail_virtual_server(request, device_id):
    return render(request, 
                  ['api_and_function.html'], 
                  {
                   # 'debug': debug_area(device_id),
                   'device_type': "Virtual Server",
                   'device_info': get_device_info_by_id_virtual_server(device_id),
                   'start_date': date_transform(get_device_info_by_id_virtual_server(device_id)['provisionDate']),
                   'motherboard': '', 
                   'powersupply': '',
                   'drivecontroller': '',
                   'virtual_server_credential': get_virtual_server_credential(device_id),
                   'ip_address_baremetal': '',
                   'default_dateway_baremetal': '',
                   'subnet_mask_baremetal': '',
                   'network_interface': '',
                   'api_doc_md': api_doc_md('device/device_detail_virtual_server.md'),
                  },
                )
# ------------- URL-Handler Functions Ends ----------- #