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
def debug_area(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getObject' +'.json?objectMask=mask[operatingSystem.passwords]';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict['operatingSystem']['passwords'];    

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

    for item in item_dict:
        temp = item['provisionDate'].partition('T')[0] 
        temp += ' '
        temp += item['provisionDate'].partition('T')[2][:8]
        temp += '(UTC'
        temp += item['provisionDate'].partition('T')[2][8:] + ')'
        item['provisionDate'] = temp

    return item_dict;  

def list_hourly_virtual_server():
    ret = APIHandler.functionHandler(APIHandler(
                      serviceName='SoftLayer_Account',
                      methodName='getHourlyVirtualGuests', 
                      mask='location',
                    ));
    item_dict = json.loads(ret);

    for item in item_dict: # Get virtual server location #
        requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Virtual_Guest' +'/'+ str(item['id']) + '/' + 'getServerRoom' +'.json?objectMask=mask[pathString]';
        s = requests.Session();
        response = s.get(requestURL);
        item['pathString'] = json.loads(response.text)['pathString']

    for item in item_dict:
        temp = item['provisionDate'].partition('T')[0] 
        temp += ' '
        temp += item['provisionDate'].partition('T')[2][:8]
        temp += '(UTC'
        temp += item['provisionDate'].partition('T')[2][8:] + ')'
        item['provisionDate'] = temp

    return item_dict;  

def list_monthly_virtual_server():
    ret = APIHandler.functionHandler(APIHandler(
                      serviceName='SoftLayer_Account',
                      methodName='getMonthlyVirtualGuests', 
                      mask='location',
                    ));
    item_dict = json.loads(ret);

    for item in item_dict: # Get virtual server location #
        requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Virtual_Guest' +'/'+ str(item['id']) + '/' + 'getServerRoom' +'.json?objectMask=mask[pathString]';
        s = requests.Session();
        response = s.get(requestURL);
        item['pathString'] = json.loads(response.text)['pathString']

    for item in item_dict:
        temp = item['provisionDate'].partition('T')[0]
        temp += ' '
        temp += item['provisionDate'].partition('T')[2][:8]
        temp += '(UTC'
        temp += item['provisionDate'].partition('T')[2][8:] + ')'
        item['provisionDate'] = temp

    return item_dict;

def date_transform(date):
    temp = date.partition('T')[0] 
    temp += ' '
    temp += date.partition('T')[2][:8]
    temp += '(UTC'
    temp += date.partition('T')[2][8:] + ')'    
    return temp

def api_doc_md(file_path):
    with open(file_path, 'r',encoding = 'utf8') as content_file:
        ret = content_file.read();
    markdown2.markdown(ret)
    return markdown2.markdown(ret, extras=['tables']);

def get_device_info_by_id_baremetal(device_id):    
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getObject' +'.json'+'?objectMask=topLevelLocation';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;

def get_start_date(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getObject' +'.json';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    date = item_dict['provisionDate'][:10] + ' ' + item_dict['provisionDate'][11:19] + '(UTC' + item_dict['provisionDate'][19:25] + ')';
    return date;    

def get_device_info_by_id_virtual_server(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Virtual_Guest' +'/'+ device_id + '/' + 'getObject' +'.json?objectMask=mask[location,operatingSystem]';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);

    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Virtual_Guest' +'/'+ device_id + '/' + 'getServerRoom' +'.json?objectMask=mask[pathString]';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict['pathString'] = json.loads(response.text)['pathString'];

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
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getObject' +'.json?objectMask=mask[operatingSystem.passwords]';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);

    for item in item_dict['operatingSystem']['passwords']:
        temp = item['modifyDate'].partition('T')[0] 
        temp += ' '
        temp += item['modifyDate'].partition('T')[2][:8]
        temp += '(UTC'
        temp += item['modifyDate'].partition('T')[2][8:] + ')'
        item['modifyDate'] = temp

    return item_dict['operatingSystem']['passwords'];    

def get_ip_address_baremetal(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Account' +'/' + 'getHardware' +'.json';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);

    for d in item_dict:
        if d['id'] == int(device_id):
            return d

def get_default_gateway_baremetal(device_id):
    ipAddr = []
    ipAddr.append(get_ip_address_baremetal(device_id)['primaryIpAddress']);
    ipAddr.append(get_ip_address_baremetal(device_id)['privateIpAddress']) 
    ipAddr.append(get_ip_address_baremetal(device_id)['networkManagementIpAddress'])

    ret = []
    s = requests.Session()
    
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Network_Subnet_IpAddress' +'/' + 'getByIpAddress' +'/'+ ipAddr[0] + '.json';
    response = s.get(requestURL)
    item_dict = json.loads(response.text)
    ret.append(item_dict['subnet']['gateway'])

    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Network_Subnet_IpAddress' +'/' + 'getByIpAddress' +'/'+ ipAddr[1] + '.json';
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    ret.append(item_dict['subnet']['gateway'])

    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Network_Subnet_IpAddress' +'/' + 'getByIpAddress' +'/'+ ipAddr[2] + '.json';
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    ret.append(item_dict['subnet']['gateway'])
    
    return ret;

def get_subnet_mask_baremetal(device_id):
    ipAddr = []
    ipAddr.append(get_ip_address_baremetal(device_id)['primaryIpAddress']);
    ipAddr.append(get_ip_address_baremetal(device_id)['privateIpAddress']) 
    ipAddr.append(get_ip_address_baremetal(device_id)['networkManagementIpAddress'])

    ret = []
    s = requests.Session()
    
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Network_Subnet_IpAddress' +'/' + 'getByIpAddress' +'/'+ ipAddr[0] + '.json';
    response = s.get(requestURL)
    item_dict = json.loads(response.text)
    ret.append(item_dict['subnet']['netmask'])

    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Network_Subnet_IpAddress' +'/' + 'getByIpAddress' +'/'+ ipAddr[1] + '.json';
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    ret.append(item_dict['subnet']['netmask'])

    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Network_Subnet_IpAddress' +'/' + 'getByIpAddress' +'/'+ ipAddr[2] + '.json';
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    ret.append(item_dict['subnet']['netmask'])
    
    return ret;

def get_network_interface_baremetal(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Hardware' +'/'+ device_id + '/' + 'getObject' +'.json?objectMask=mask[primaryNetworkComponent,primaryBackendNetworkComponent,remoteManagementComponent]';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;

def get_virtual_server_credential(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Virtual_Guest' +'/'+ device_id + '/' + 'getObject' +'.json?objectMask=mask[operatingSystem.passwords]';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);

    for item in item_dict['operatingSystem']['passwords']:
        temp = item['modifyDate'].partition('T')[0] 
        temp += ' '
        temp += item['modifyDate'].partition('T')[2][:8]
        temp += '(UTC'
        temp += item['modifyDate'].partition('T')[2][8:] + ')'
        item['modifyDate'] = temp

    return item_dict['operatingSystem']['passwords'];    

def get_network_interface_virtual_server(device_id):
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Virtual_Guest' +'/'+ device_id + '/' + 'getObject' +'.json?objectMask=mask[primaryNetworkComponent,primaryBackendNetworkComponent]';
    s = requests.Session();
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    return item_dict;

def get_default_gateway_virtual_server(device_id):
    ipAddr = []
    ipAddr.append(get_network_interface_virtual_server(device_id)['primaryNetworkComponent']['primaryIpAddress'])
    ipAddr.append(get_network_interface_virtual_server(device_id)['primaryBackendNetworkComponent']['primaryIpAddress']) 

    ret = []
    s = requests.Session()
    
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Network_Subnet_IpAddress' +'/' + 'getByIpAddress' +'/'+ ipAddr[0] + '.json';
    response = s.get(requestURL)
    item_dict = json.loads(response.text)
    ret.append(item_dict['subnet']['gateway'])

    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Network_Subnet_IpAddress' +'/' + 'getByIpAddress' +'/'+ ipAddr[1] + '.json';
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    ret.append(item_dict['subnet']['gateway'])
    
    return ret;

def get_subnet_mask_virtual_server(device_id):
    ipAddr = []
    ipAddr.append(get_network_interface_virtual_server(device_id)['primaryNetworkComponent']['primaryIpAddress'])
    ipAddr.append(get_network_interface_virtual_server(device_id)['primaryBackendNetworkComponent']['primaryIpAddress']) 
    
    ret = []
    s = requests.Session()
    
    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Network_Subnet_IpAddress' +'/' + 'getByIpAddress' +'/'+ ipAddr[0] + '.json';
    response = s.get(requestURL)
    item_dict = json.loads(response.text)
    ret.append(item_dict['subnet']['netmask'])

    requestURL = 'https://'+settings.SL_USERNAME+':'+settings.SL_APIKEY+'@api.softlayer.com/rest/v3/'+ 'SoftLayer_Network_Subnet_IpAddress' +'/' + 'getByIpAddress' +'/'+ ipAddr[1] + '.json';
    response = s.get(requestURL);
    item_dict = json.loads(response.text);
    ret.append(item_dict['subnet']['netmask'])

    return ret;    

# ------------- Utility Functions Ends----------- #
