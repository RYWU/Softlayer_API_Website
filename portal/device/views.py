# device/views.py
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.conf import settings

import json
import markdown2 # Document markup usage. #
from pprint import pprint
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

# ------------- Utility Functions Starts----------- #
def debug_area(param1):
    return param1;

def count_device():
    return len( json.loads(APIHandler.functionHandler(APIHandler(serviceName = 'SoftLayer_Account', methodName = 'getHardware'))) ) + \
           len( json.loads(APIHandler.functionHandler(APIHandler(serviceName = 'SoftLayer_Account', methodName = 'getHourlyVirtualGuests'))) ) + \
           len( json.loads(APIHandler.functionHandler(APIHandler(serviceName = 'SoftLayer_Account', methodName = 'getMonthlyVirtualGuests'))) );

def list_baremetal():
    ret = APIHandler.functionHandler(APIHandler(
                      serviceName='SoftLayer_Account',
                      methodName='getHardware', 
                      mask='topLevelLocation',
                    ));
    item_dict = json.loads(ret);
    return item_dict;  

def list_hourly_virtual_server():
    ret = APIHandler.functionHandler(APIHandler(
                      serviceName='SoftLayer_Account',
                      methodName='getHourlyVirtualGuests', 
                      mask='location',
                    ));
    item_dict = json.loads(ret);
    return item_dict;  

def list_monthly_virtual_server():
    ret = APIHandler.functionHandler(APIHandler(
                      serviceName='SoftLayer_Account',
                      methodName='getMonthlyVirtualGuests', 
                      mask='location',
                    ));
    item_dict = json.loads(ret);
    return item_dict;

def api_doc_md():
    with open('device/device_list.md', 'r') as content_file:
        ret = content_file.read();
    markdown2.markdown(ret)
    return markdown2.markdown(ret, extras=['tables']);

def get_device_info_by_id_baremetal(device_id):    
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getObject' +'.json'+'?objectMask=topLevelLocation';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;

def get_device_info_by_id_virtual_server(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getObject' +'.json';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;

def get_os_baremetal(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getOperatingSystem' +'.json';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;

def get_ram_baremetal(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getMemory' +'.json';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;    

def get_processors(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getProcessors' +'.json';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;

def get_motherboard(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getMotherboard' +'.json';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;

def get_power_supply(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getPowerSupply' +'.json';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;

def get_drive_controller(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getDriveControllers' +'.json';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;

def get_baremetal_credential(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getRemoteManagementAccounts' +'.json';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;

# ------------- Utility Functions Ends----------- #


# ------------- URL-Handler Functions Starts----------- #
def device(request):
    return render(request, ['api_and_function.html'])

def device_list(request):
    return render(request, 
                  ['api_and_function.html'], 
                  {
                   'total_devices_number': count_device(),
                   'baremetal': list_baremetal(),
                   'hourlyvirtualserver': list_hourly_virtual_server(),
                   'monthlyvirtualserver': list_monthly_virtual_server(),
                   # 'api_list': api_list(),
                   'api_doc_md': api_doc_md(), 
                  },
                )

def device_detail_baremetal(request, device_id):
    return render(request, 
                  ['api_and_function.html'], 
                  {
                   'debug': debug_area(device_id),
                   'device_type': "Bare Metal",
                   'os': get_os_baremetal(device_id),
                   'ram': get_ram_baremetal(device_id),
                   'processor': get_processors(device_id),
                   'motherboard': get_motherboard(device_id), 
                   'device_info': get_device_info_by_id_baremetal(device_id), 
                   'powersupply': get_power_supply(device_id),
                   'drivecontroller': get_drive_controller(device_id),
                   'baremetal_username': get_baremetal_credential(device_id),
                   'baremetal_password': get_baremetal_credential(device_id),
                  },
                )

def device_detail_virtual_server(request, device_id):
    return render(request, 
                  ['api_and_function.html'], 
                  {
                   'debug': debug_area(device_id),
                   'device_type': "Virtual Server",
                   'device_info': get_device_info_by_id_virtual_server(device_id), 
                  },
                )
# ------------- URL-Handler Functions Ends ----------- #
