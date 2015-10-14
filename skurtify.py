#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import *
import json
import spotipy
from spotipytest import spotip
from assr import test_sr

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
	sr_play, text, time = test_sr(request)
	search_result = spotip(sr_play)

	if search_result['tracks']['next'] == None:
		tracks = sr_play + " (Not avalible on spotify)"
		pic = "http://www.clipartbest.com/cliparts/niX/nX7/niXnX7E5T.gif"
		url = "http://localhost:8080"
		url_pic = '../static/bilder/nospotify.png'

		return template ("search", tracks=tracks, pic=pic, url=url, url_pic=url_pic, text=text, time=time)

	else:
		for item in search_result['tracks']['items']:
			tracks = sr_play
			pic = item['album']['images'][0]['url']
			url = item['external_urls']['spotify']
			url_pic = '../static/bilder/spotify.png'

		return template ("search", tracks=tracks, pic=pic, url=url, url_pic=url_pic, text=text, time=time)


run(host='localhost', port=8080, debug=True, reloader=True)