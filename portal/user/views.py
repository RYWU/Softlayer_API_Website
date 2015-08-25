from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
import requests,json,base64,http.client,markdown2

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



def account(request):
	 return render(request, ['account.html']);

def api_user_doc():
    with open('User/user_doc.md', 'r',encoding = 'utf8') as content_file:
        ret = content_file.read();
    print (ret);
    markdown2.markdown(ret)
    return markdown2.markdown(ret, extras=['tables']);

def api_profile_doc():
    with open('User/profile_doc.md', 'r',encoding = 'utf8') as content_file:
        ret = content_file.read();
    print (ret);
    markdown2.markdown(ret)
    return markdown2.markdown(ret, extras=['tables']);

def api_internpro_doc():
    with open('User/internpro_doc.md', 'r',encoding = 'utf8') as content_file:
        ret = content_file.read();
    print (ret);
    markdown2.markdown(ret)
    return markdown2.markdown(ret, extras=['tables']);


def user(request):
	res = {'method':'getUser','objectid':'398983'}
	api = restapi('User_Customer_ApiAuthentication',**res)
	test = api + '?objectMask=apiAuthenticationKeys;childUsers'
	get = requests.get(test)
	doc1 = json.loads(get.text)

	res1 = {'method':'getUser','objectid':'399465'}
	api1 = restapi('User_Customer_ApiAuthentication',**res1)
	test1 = api1 + '?objectMask=apiAuthenticationKeys'
	get1 = requests.get(test1)
	doc2 = json.loads(get1.text)
	return render(request,'user.html',{'doc1':doc1,'doc2':doc2,'api_user_doc': api_user_doc()})


def profile(request):
	res = {'method':'getUser','objectid':'398983'}
	api = restapi('User_Customer_ApiAuthentication',**res)
	test = api + '?objectMask=apiAuthenticationKeys;childUsers'
	get = requests.get(test)
	doc1 = json.loads(get.text)

	res1 = {'method':'getUser','objectid':'399465'}
	api1 = restapi('User_Customer_ApiAuthentication',**res1)
	test1 = api1 + '?objectMask=apiAuthenticationKeys'
	get1 = requests.get(test1)
	doc2 = json.loads(get1.text)

	res3 = {'method':'getObject','objectid':'398983'}
	api3 = restapi('Account_Password',**res3)
	#test1 = api1 + '?objectMask=apiAuthenticationKeys'
	get3 = requests.get(api3)
	doc3 = json.loads(get3.text)
	return render(request,'profile.html',{'doc1':doc1,'doc2':doc2,'doc3':doc3,'api_profile_doc':api_profile_doc()})

def internpro(request):
	res = {'method':'getUser','objectid':'398983'}
	api = restapi('User_Customer_ApiAuthentication',**res)
	test = api + '?objectMask=apiAuthenticationKeys;childUsers'
	get = requests.get(test)
	doc1 = json.loads(get.text)

	res1 = {'method':'getUser','objectid':'399465'}
	api1 = restapi('User_Customer_ApiAuthentication',**res1)
	test1 = api1 + '?objectMask=apiAuthenticationKeys'
	get1 = requests.get(test1)
	doc2 = json.loads(get1.text)
	return render(request,'internpro.html',{'doc1':doc1,'doc2':doc2,'api_internpro_doc':api_internpro_doc()})
