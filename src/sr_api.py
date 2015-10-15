#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import urlopen
from json import load
from channel import channel
from song_time import song_time

def sr_api(request):
	'''Runs sr:s api and catches song, artist and time it played. Catches also channel name'''
	request = request.query['channel']
	channel_name = channel(request)
	url = "http://api.sr.se/api/v2/playlists/rightnow?channelid="+request+"&format=json"
	response = urlopen(url)
	sr_json = load(response)
	try:
		song = sr_json['playlist']['song']['description']
		text = 'Right now on ' + channel_name
		time = song_time(sr_json)
		return (song, text, time)
	except KeyError:
		try:
			song = sr_json['playlist']['previoussong']['description']
			text = 'Nothing playing right now, previous song on ' + channel_name + ' was'
			time = song_time(sr_json)
			return (song, text, time)
		except KeyError:
			song = sr_json['playlist']['nextsong']['description']
			text = 'Nothing playing right now, next song on ' + channel_name + ' is'
			time = song_time(sr_json)
			return (song, text, time)