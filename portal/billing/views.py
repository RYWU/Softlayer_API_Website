from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
import requests,json,base64,http.client,markdown2
# Create your views here.
username = settings.SL_USERNAME
api_key = settings.SL_API_KEY

def restapi(servicename,**kwargs):
	if (len(kwargs) == 4):
		apiurl = ("https://" + username + ":" + api_key +"@api.softlayer.com/rest/v3/SoftLayer_%s/%s/%s/%s/%s" + ".json") % (servicename,kwargs['serverid'], kwargs['method'],kwargs['objectid'],kwargs['objectmethod'])
	elif (len(kwargs) == 3):
		if ('serverid' in kwargs):
			apiurl = ("https://" + username + ":" + api_key +"@api.softlayer.com/rest/v3/SoftLayer_%s/%s/%s/%s" + ".json") % (servicename,kwargs['serverid'], kwargs['method'],kwargs['objectid'])
		else:
			apiurl = ("https://" + username + ":" + api_key +"@api.softlayer.com/rest/v3/SoftLayer_%s/%s/%s/%s" + ".json") % (servicename, kwargs['method'],kwargs['objectid'],kwargs['objectmethod'])
	elif (len(kwargs) == 2):
		if ('serverid' in kwargs):
			apiurl = ("https://" + username + ":" + api_key +"@api.softlayer.com/rest/v3/SoftLayer_%s/%s/%s" + ".json") % (servicename,kwargs['serverid'], kwargs['method'])
		else:
			apiurl = ("https://" + username + ":" + api_key +"@api.softlayer.com/rest/v3/SoftLayer_%s/%s/%s" + ".json") % (servicename,kwargs['method'], kwargs['objectid'])
	elif (len(kwargs) == 1):
		if ('serverid' in kwargs):
			apiurl = ("https://" + username + ":" + api_key +"@api.softlayer.com/rest/v3/SoftLayer_%s/%s" + ".json") % (servicename,kwargs['serverid'])
		else:
			apiurl = ("https://" + username + ":" + api_key +"@api.softlayer.com/rest/v3/SoftLayer_%s/%s" + ".json") % (servicename,kwargs['method'])
	else:
		apiurl = ("https://" + username + ":" + api_key +"@api.softlayer.com/rest/v3/SoftLayer_%s" + ".json") % (servicename)

	return apiurl



def api_billing_doc():
    with open('Billing/billing_doc.md', 'r') as content_file:
        ret = content_file.read();
    markdown2.markdown(ret)
    return markdown2.markdown(ret, extras=['tables']);



def billing(request):

	res1 = {'method':'getLatestRecurringInvoice'}
	api1 = restapi('Account',**res1)
	test1 = api1 + '?objectMask=id;invoiceTotalRecurringAmount;invoiceTotalRecurringTaxAmount;invoiceTotalOneTimeAmount;invoiceTotalOneTimeTaxAmount;invoiceTotalAmount'
	get1 = requests.get(test1)
	doc1 = json.loads(get1.text)

	
	return render(request,'billing.html',{
		'doc1': doc1,
		'get_Invoice_by_se':get_Invoice_by_se(),
		'get_Invoice_by_ks':get_Invoice_by_ks(),
		'get_Invoice_by_ag':get_Invoice_by_ag(),
		'get_Invoice_by_tt':get_Invoice_by_tt(),
		'api_billing_doc':api_billing_doc
		})
	

def get_Invoice_by_se():
	res5 = {'method':'getAllBillingItems'}
	api5 = restapi('Account',**res5)
	test = api5 + '?resultLimit=0,200'
	get5 = requests.get(test)
	billing_item = json.loads(get5.text)

	group_se = []
	for item in range(len(billing_item)):
		if 'se-' in billing_item[item]['hostName'][0:3]:
			group_se.append([billing_item[item]['hostName'],billing_item[item]['recurringFee']])
	return group_se

def get_Invoice_by_ks():
	res5 = {'method':'getAllBillingItems'}
	api5 = restapi('Account',**res5)
	test = api5 + '?resultLimit=0,200'
	get5 = requests.get(test)
	billing_item = json.loads(get5.text)

	group_ks = []
	for item in range(len(billing_item)):
		if 'ks-' in billing_item[item]['hostName'][0:3]:
			group_ks.append([billing_item[item]['hostName'],billing_item[item]['recurringFee']])
	return group_ks


def get_Invoice_by_ag():
	res5 = {'method':'getAllBillingItems'}
	api5 = restapi('Account',**res5)
	test = api5 + '?resultLimit=0,200'
	get5 = requests.get(test)
	billing_item = json.loads(get5.text)

	group_ag = []
	for item in range(len(billing_item)):
		if 'ag-' in billing_item[item]['hostName'][0:3]:
			group_ag.append([billing_item[item]['hostName'],billing_item[item]['recurringFee']])

	return group_ag

def get_Invoice_by_tt():
	res5 = {'method':'getAllBillingItems'}
	api5 = restapi('Account',**res5)
	test = api5 + '?resultLimit=0,200'
	get5 = requests.get(test)
	billing_item = json.loads(get5.text)

	group_tt = []
	for item in range(len(billing_item)):
		if 'tt-' in billing_item[item]['hostName'][0:3]:
			group_tt.append([billing_item[item]['hostName'],billing_item[item]['recurringFee']])

	return group_tt

