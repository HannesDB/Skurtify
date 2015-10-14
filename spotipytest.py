#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spotipy
from bottle import route, static_file

def spotip(input_search):
	sp = spotipy.Spotify()
	print sp
	results = sp.search(q=input_search, limit=1)
	print results
	return results