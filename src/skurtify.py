#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import *
import json
import spotipy
from spotip import spotip
from sr_api import sr_api

@route("/static/<filepath:path>")
def server_static(filepath):
	"""CSS"""
	return static_file(filepath, root="static")

@route('/')
def start():
	'''Mainpage'''
	return template ("index")

@route('/search/')
def get_track():
	'''search'''
	song, text, time = sr_api(request)
	search_result = spotip(song)

	if search_result['tracks']['next'] == None:
		tracks = song + " (Not avalible on spotify)"
		pic = "http://www.clipartbest.com/cliparts/niX/nX7/niXnX7E5T.gif"
		url = "http://localhost:8080"
		url_pic = '../static/bilder/nospotify.png'
		
		if request.headers.get('Accept') == "application/json":
			response.set_header("Content-Type", "application/json")
			return json.dumps(song)
		else:
			return template ("search", tracks=tracks, pic=pic, url=url, url_pic=url_pic, text=text, time=time)

	else:
		for item in search_result['tracks']['items']:
			tracks = song
			pic = item['album']['images'][0]['url']
			url = item['external_urls']['spotify']
			url_pic = '../static/bilder/spotify.png'

		if request.headers.get('Accept') == "application/json":
			response.set_header("Content-Type", "application/json")
			return json.dumps(song)
		else:
			return template ("search", tracks=tracks, pic=pic, url=url, url_pic=url_pic, text=text, time=time)


run(host='localhost', port=8080, debug=True, reloader=True)