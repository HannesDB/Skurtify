#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spotipy

def spotip(song):
	'''search for song on spotify'''
	song = song.replace("ft. ", "", 5)
	song = song.replace("& ", "", 5)
        
##        for item in song:
##                if item == "å" or item == "ä":
##                        song = song.replace(item, "a")
##
##        for item in song:
##                if item == "ö":
##                        song = song.replace(item, "o")
                        
	sp = spotipy.Spotify()
	results = sp.search(q=song, limit=1)
	# print results
	# print song

	if results['tracks']['total'] == 0:
		pic = "http://static.photo.net/attachments/bboard/00I/00IkUN-33436284.gif"
		url = "#"
		url_pic = '../static/bilder/nospotify.png'
		return (pic, url, url_pic)

	else:
		for item in results['tracks']['items']:
			pic = item['album']['images'][0]['url']
			url = item['external_urls']['spotify']
			url_pic = '../static/bilder/spotify.png'
			return (pic, url, url_pic)
