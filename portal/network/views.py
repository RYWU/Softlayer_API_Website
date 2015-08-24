from django.shortcuts import render

# ------------- Utility Functions Starts ----------- #
from portal.utils import *

def baremetal_info():
    ret = APIHandler.functionHandler(APIHandler(
                      serviceName='SoftLayer_Account',
                      methodName='getHardware', 
                      mask='topLevelLocation',
                    ));
    item_dict = json.loads(ret);

    for item in item_dict:
        temp = item['provisionDate'].partition('T')[0] 
        temp += ' '
        temp += item['provisionDate'].partition('T')[2][:8]
        temp += '(UTC'
        temp += item['provisionDate'].partition('T')[2][8:] + ')'
        item['provisionDate'] = temp

    for item in item_dict: # Get Allocation data #
        requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ str(item['id']) + '/' + 'getBandwidthAllocation' +'.json';
        s = requests.Session();
        response = s.get(requestURL);
        item['allocation'] = response.text[1:-1]

    for item in item_dict: # Get inbound outbound bandwidth data #
        requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ str(item['id']) + '/' + 'getObject' +'.json?objectMask=mask[inboundBandwidthUsage,outboundBandwidthUsage]';
        s = requests.Session();
        response = s.get(requestURL);
        item['inboundBandwidthUsage'] = round(1024 * float(json.loads(response.text)['inboundBandwidthUsage']), 2);
        item['outboundBandwidthUsage'] = round(1024 * float(json.loads(response.text)['outboundBandwidthUsage']), 2);
        item['totalBandwidthUsage'] = round( (1024 * float(json.loads(response.text)['inboundBandwidthUsage'])+1024 * float(json.loads(response.text)['outboundBandwidthUsage'])) , 2);

    return item_dict;  

def hourly_virtual_server_info():
    ret = APIHandler.functionHandler(APIHandler(
                      serviceName='SoftLayer_Account',
                      methodName='getHourlyVirtualGuests', 
                      mask='location',
                    ));
    item_dict = json.loads(ret);

    for item in item_dict:
        temp = item['provisionDate'].partition('T')[0] 
        temp += ' '
        temp += item['provisionDate'].partition('T')[2][:8]
        temp += '(UTC'
        temp += item['provisionDate'].partition('T')[2][8:] + ')'
        item['provisionDate'] = temp

    for item in item_dict: # Get Allocation data #
        item['allocation'] = 'Pay As You Go'

    for item in item_dict: # Get inbound outbound bandwidth data #
        requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Virtual_Guest' +'/'+ str(item['id']) + '/' + 'getObject' +'.json?objectMask=mask[inboundPublicBandwidthUsage,outboundPublicBandwidthUsage]';
        s = requests.Session();
        response = s.get(requestURL);
        item['inboundBandwidthUsage'] = round(1024 * float(json.loads(response.text)['inboundPublicBandwidthUsage']), 2);
        item['outboundBandwidthUsage'] = round(1024 * float(json.loads(response.text)['outboundPublicBandwidthUsage']), 2);
        item['totalBandwidthUsage'] = round( (1024 * float(json.loads(response.text)['inboundPublicBandwidthUsage'])+1024 * float(json.loads(response.text)['outboundPublicBandwidthUsage'])) , 2);

    for item in item_dict: # Get Server location #
        requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Virtual_Guest' +'/'+ str(item['id']) + '/' + 'getServerRoom' +'.json?objectMask=mask[pathString]';
        s = requests.Session();
        response = s.get(requestURL);
        item['pathString'] = json.loads(response.text)['pathString']        

    return item_dict;  

def monthly_virtual_server_info():
    ret = APIHandler.functionHandler(APIHandler(
                      serviceName='SoftLayer_Account',
                      methodName='getMonthlyVirtualGuests', 
                      mask='location',
                    ));
    item_dict = json.loads(ret);

    # for item in item_dict:
    #     temp = item['provisionDate'].partition('T')[0] 
    #     temp += ' '
    #     temp += item['provisionDate'].partition('T')[2][:8]
    #     temp += '(UTC'
    #     temp += item['provisionDate'].partition('T')[2][8:] + ')'
    #     item['provisionDate'] = temp

    for item in item_dict: # Get Allocation data #
        requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Virtual_Guest' +'/'+ str(item['id']) + '/' + 'getBandwidthAllocation' +'.json';
        s = requests.Session();
        response = s.get(requestURL);
        item['allocation'] = response.text[1:-1]

    for item in item_dict: # Get inbound outbound bandwidth data #
        requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Virtual_Guest' +'/'+ str(item['id']) + '/' + 'getObject' +'.json?objectMask=mask[inboundPublicBandwidthUsage,outboundPublicBandwidthUsage]';
        s = requests.Session();
        response = s.get(requestURL);
        item['inboundBandwidthUsage'] = round(1024 * float(json.loads(response.text)['inboundPublicBandwidthUsage']), 2);
        item['outboundBandwidthUsage'] = round(1024 * float(json.loads(response.text)['outboundPublicBandwidthUsage']), 2);
        item['totalBandwidthUsage'] = round( (1024 * float(json.loads(response.text)['inboundPublicBandwidthUsage'])+1024 * float(json.loads(response.text)['outboundPublicBandwidthUsage'])) , 2);

    for item in item_dict: # Get Server location #
        requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Virtual_Guest' +'/'+ str(item['id']) + '/' + 'getServerRoom' +'.json?objectMask=mask[pathString]';
        s = requests.Session();
        response = s.get(requestURL);
        item['pathString'] = json.loads(response.text)['pathString']        

    return item_dict;

# ------------- Utility Functions Ends----------- #

def debug():
    return 'debug function works!'

def bandwidth_summary(request):
    return render(request, 
                    ['api_and_function.html'],
                    {
                       'total_devices_number': count_device(),
                       'baremetal': baremetal_info(),
                       'hourlyvirtualserver': hourly_virtual_server_info(),
                       'monthlyvirtualserver': monthly_virtual_server_info(),

                       'api_doc_md': api_doc_md('network/doc/bandwidth_summary.md'),
                       'debug': debug(),
                    }
                );