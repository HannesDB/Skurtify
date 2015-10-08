#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://jsonlint.com/

from bottle import *
import json
import spotipy
from spotipytest import spotip

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
	input_search = request.forms.search
	ids = []
	tracks = []
	art = []
	search_result = spotip(input_search)
	for i, item in enumerate(search_result['tracks']['items'], start=1):
		ids.append(i)
		tracks.append(item['name'])
		art.append(item['artists'][0]['name'])
	return template ("show", tracks=tracks, ids=ids, art=art)

	

run(host='localhost', port=8080, debug=True, reloader=True)