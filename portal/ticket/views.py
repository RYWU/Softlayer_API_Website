from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
from Ticket.models import Post
import requests,json,base64,http.client,markdown2
# Create your views here.
username = settings.SL_USERNAME
api_key = settings.SL_API_KEY

def restapi(servicename,**kwargs):
	if (len(kwargs) == 4):
		apiurl = ("https://" + username + ":" + api_key +"@api.softlayer.com/rest/v3/SoftLayer_%s/%s/%s/%s/%s" + ".json") % (servicename,kwargs['serverid'], kwargs['method'],kwargs['objectid'],kwargs['objectmethod'])
	elif (len(kwargs) == 3):
		apiurl = ("https://" + username + ":" + api_key +"@api.softlayer.com/rest/v3/SoftLayer_%s/%s/%s/%s" + ".json") % (servicename,kwargs['serverid'], kwargs['method'],kwargs['objectid'])
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


def support(request):
	 return render(request, ['support.html']);


def api_doc():
    with open('Ticket/doc.md', 'r',encoding = 'utf8') as content_file:
        ret = content_file.read();
    print (ret);
    markdown2.markdown(ret)
    return markdown2.markdown(ret, extras=['tables']);

def ticket(request):

	res = {'method':'getTickets'}
	api = restapi('Account',**res)
	get = requests.get(api)
	doc = json.loads(get.text)

	res3 = {'method':'getObject','objectid':'21079179'}
	api3 = restapi('Ticket',**res3)
	#test1 = api3 + '?objectMask=editor'
	get3 = requests.get(api3)
	doc3 = json.loads(get3.text)

	new_ticket = Post.objects.all()

	return render(request,'ticket.html',{'doc1': doc[0],'doc2':doc[1],'new_ticket':new_ticket,'api_doc': api_doc()})

def getCurrentUser():
	res = {'method':'getCurrentUser'}
	api = restapi('Account',**res)
	get = requests.get(api)
	current_user = json.loads(get.text)
	return current_user


def create_ticket(title=None, body=None, subject=None):
	current_user = getCurrentUser()
	new_ticket = {"parameters":[[{'subjectId': 'subject','contents': 'body','assignedUserId': current_user['username'],'title': 'title',}]]}
	encoded_new_ticket = json.dumps(new_ticket)
	
 #https://[username]:[apiKey]@api.[service.]softlayer.com/rest/v3/[serviceName]/[initializationParameter].[returnDatatype]
	api = 'https://'+ username + ':' + api_key +'@api.softlayer.com/rest/v3/Ticket/createStandardTicket/' + encoded_new_ticket + '.json'
	get = requests.get(api)
	created_ticket = json.loads(get.text)
	return created_ticket



