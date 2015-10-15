#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spotipy

def spotip(input_search):
	'''search for song on spotify'''
	sp = spotipy.Spotify()
	results = sp.search(q=input_search, limit=1)
	return results