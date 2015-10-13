#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import urlopen
from json import load

def test_sr():
	'''testar sr:s api'''
	url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164&format=json"
	response = urlopen(url)
	json_obj = load(response)
	try:
		obj = json_obj['playlist']['song']['description']
		return obj
	except KeyError:
		try:
			obj = json_obj['playlist']['nextsong']['description']
			return obj
		except KeyError:
			obj = json_obj['playlist']['previoussong']['description']
			return obj

	'''
	#Se JSONkod vid behov
	mer_kod = raw_input("Se JSONkod? Y/N: ")
	if mer_kod == "Y" or mer_kod == "y":
	    print json_obj
	'''