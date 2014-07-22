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

def test(request):
	name = "test"
	context = {'name' : [name]}
	return render_to_response('graph.html', context)

def generate(request):
	code = request.GET['code']
	print code

	

	data = {'client_id': '50831fa41c5a4d3cba82f9bd14bb4a86', 'client_secret' : 'fd9652076534434eb4550015b119a417','grant_type':'authorization_code','code':code, 'redirect_uri':'http://localhost:8000/gen'}
	r = requests.post('https://api.instagram.com/oauth/access_token', data=data)
	
	u_id = r.json()['user']['id']
	token = r.json()['access_token']
	followers = []
	print u_id
	print token
	

	x = requests.get('https://api.instagram.com/v1/users/'+str(u_id)+'/followed-by?access_token='+token)
	y = x.json()['data']
	
	
	

	for i in y:
		followers.append(i['id'])
	
	activity = []
	for i in followers:
		p = requests.get('https://api.instagram.com/v1/users/'+i+'/media/recent/?access_token='+token)

	q = p.json()['data']
	
	
	time = []
	for j in q:
		time.append(j['created_time'])
	print time
	

	
	converted_time = []
	for k in time:
		converted_time.append(
    datetime.datetime.fromtimestamp(
        int(k)
    ).strftime('%Y-%m-%d %H:%M:%S')
)    
	print converted_time

	
	dates = []
	for i in converted_time:
		f = int(i.split()[1].split(':')[0])
		l = int(i.split()[1].split(':')[1])
		if l>30:
			f+=1
			if f> 24:
				f=1;
		dates.append(i.split()[0] + "," + str(f))
	timings = []
	# for i in converted_time:
	# 	timings.append(i.split()[1])
	print ("\n").join(dates)
	"""
	print "test"	#print timings
			f = int(i.split(':')[0])
		l = int(i.split(':')[1])
		if l>30:
		for i	for i in  in 		f+=1

	print dates
	newtime = []
	for i in timingsstr(:)
	fsplit(':')[0])
		l = int(i.split(':')[1])
		if l>30:
			f+=1
		newtime.append(f)
	print newtime
	
	#a = json.dumps(timings)
	context = { 'dates' : dates, 'newtime' : newtime}
	print context
	"""
	date_string = "Date,Timings\\n" + ("\\n").join(dates)
	context = {'date_string' : date_string}
	return render_to_response('graph.html', context)
	"""
	return HttpResponse(context, mimetype='application/json')
	
	return HttpResponseRedirect('/test')
	"""







	#datetime.datetime.fromtimestamp(1401517139).strftime('%H:%M:%S')



