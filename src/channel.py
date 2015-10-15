#!/usr/bin/env python
# -*- coding: utf-8 -*-

def channel(request):
	'''writes channel name'''
	if request == "132":
		return "P1"

	elif request == "163":
		return "P2"

	elif request == "164":
		return "P3"

	elif request == "220":
		return "P4 Halland"
