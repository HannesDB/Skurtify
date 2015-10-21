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
	pic, url, url_pic = spotip(song)

	if request.headers.get('Accept') == "application/json":
		response.set_header("Content-Type", "application/json")
		json_obj = {"song": {"song": song, "spotify_url": url, "sr_playtime": time}}
		return json.dumps(json_obj)
	else:
		return template ("search", tracks=song, pic=pic, url=url, url_pic=url_pic, text=text, time=time)


run(host='localhost', port=8080, debug=True, reloader=True)