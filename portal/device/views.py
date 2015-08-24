# device/views.py
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.conf import settings

# ------------- Utility Functions Starts ----------- #
from portal.utils import *
# ------------- Utility Functions Ends----------- #

# ------------- URL-Handler Functions Starts----------- #

def device_list(request):
    return render(request, 
                  ['api_and_function.html'], 
                  {
                   'total_devices_number': count_device(),
                   'baremetal': list_baremetal(),
                   'hourlyvirtualserver': list_hourly_virtual_server(),
                   'monthlyvirtualserver': list_monthly_virtual_server(),
                   'api_doc_md': api_doc_md('device/doc/device_list.md'), 
                   # 'api_list': api_list(),
                   # 'debug': debug_area(),
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
                   'network_interface': get_network_interface_baremetal(device_id),
                   'api_doc_md': api_doc_md('device/doc/device_detail_baremetal.md'),
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
                   'virtual_server_credential': get_virtual_server_credential(device_id),
                   'ip_address_virtual_server': get_network_interface_virtual_server(device_id),
                   'default_dateway_virtual_server': get_default_gateway_virtual_server(device_id),
                   'subnet_mask_virtual_server': get_subnet_mask_virtual_server(device_id),
                   'network_interface': get_network_interface_virtual_server(device_id),
                   'api_doc_md': api_doc_md('device/doc/device_detail_virtual_server.md'),
                  },
                )
# ------------- URL-Handler Functions Ends ----------- #