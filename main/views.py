from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response

from urllib2 import urlopen
import datetime


import requests
import json


import time
import datetime





class IndexView(TemplateView):
	template_name = "index.html"

pass


def generate(request):
	code = request.GET['code']
	print code

	

	data = {'client_id': '50831fa41c5a4d3cba82f9bd14bb4a86', 'client_secret' : 'fd9652076534434eb4550015b119a417','grant_type':'authorization_code','code':code, 'redirect_uri':'http://localhost:8000/gen'}
	r = requests.post('https://api.instagram.com/oauth/access_token', data=data)
	
	#print r.json()
	
	u_id = r.json()['user']['id']
	token = r.json()['access_token']
	#print code
	#print u_id
	#print token
	followers = []
	print u_id
	print token
	

	x = requests.get('https://api.instagram.com/v1/users/'+str(u_id)+'/followed-by?access_token='+token)
	y = x.json()['data']
	print y
	print "| data"
	

	for i in y:
		followers.append(i['id'])
	print followers
	activity = []
	for i in followers:
		p = requests.get('https://api.instagram.com/v1/users/'+i+'/media/recent/?access_token='+token)

	q = p.json()['data']
	print q
	
	time = []
	for j in q:
		time.append(j['created_time'])
	print time
	

	##
	converted_time = []
	for k in time:
		print(
    datetime.datetime.fromtimestamp(
        int(k)
    ).strftime('%Y-%m-%d %H:%M:%S')
)
		#datetime.datetime.fromtimestamp(k).strftime('%H:%M:%S')

	#print converted_time

	return HttpResponseRedirect('/test')
	







	#datetime.datetime.fromtimestamp(1401517139).strftime('%H:%M:%S')



