#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import urlopen
from json import load
from chann import chann
from datetimetest import song_time

def test_sr(request):
	'''testar sr:s api'''
	request = request.query['channel']
	channel_name = chann(request)
	url = "http://api.sr.se/api/v2/playlists/rightnow?channelid="+request+"&format=json"
	response = urlopen(url)
	json_obj = load(response)
	try:
		obj = json_obj['playlist']['song']['description']
		text = 'Right now on ' + channel_name
		time = song_time(json_obj)
		return (obj, text, time)
	except KeyError:
		try:
			obj = json_obj['playlist']['previoussong']['description']
			text = 'Nothing playing right now, previous song on ' + channel_name + ' was'
			time = song_time(json_obj)
			return (obj, text, time)
		except KeyError:
			obj = json_obj['playlist']['nextsong']['description']
			text = 'Nothing playing right now, next song on ' + channel_name + ' is'
			time = song_time(json_obj)
			return (obj, text, time)