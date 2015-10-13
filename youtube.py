#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import urlopen
from json import load


def you_api(sr_play):
	'''testar sr:s api'''
	url = "https://www.googleapis.com/freebase/v1/search?,"+sr_play
	print url
	response = urlopen(url)
	j_obj = load(response)
	print j_obj
	return j_obj
	
