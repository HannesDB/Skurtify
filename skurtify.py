#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import *
import json
import spotipy
from spotipytest import spotip
from assr import test_sr
from youtube import you_api

@route("/static/<filepath:path>")
def server_static(filepath):
	"""CSS"""
	return static_file(filepath, root="static")

@route('/')
def start():
	'''Mainpage'''
	return template ("index")

@route('/search/', method='POST')
def get_track():
	'''search'''
	sr_play, text = test_sr()
	tracks = []
	art = []
	pic = []
	url = []

	search_result = spotip(sr_play)

	for item in search_result['tracks']['items']:
		tracks = item['name']
		art = item['artists'][0]['name']
		pic = item['album']['images'][0]['url']
		url = item['external_urls']['spotify']


	return template ("search", tracks=tracks, art=art, pic=pic, url=url, text=text)

	

run(host='localhost', port=8080, debug=True, reloader=True)