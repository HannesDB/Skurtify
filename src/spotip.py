#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spotipy

def spotip(song):
	'''search for song on spotify'''
	sp = spotipy.Spotify()
	results = sp.search(q=song, limit=1)
	print results
	print song

	if results['tracks']['next'] == None:
                #Test för att plocka bort &-tecken i söksträngen 
##              for item in song:
##                      if item == "&":
##                              new_song = song.replace(item, "")
		li = (song.split('-'))
		sp = spotipy.Spotify()
		results = sp.search(q=li[1], limit=1)

		for item in results['tracks']['items']:
			pic = item['album']['images'][0]['url']
			url = item['external_urls']['spotify']
			url_pic = '../static/bilder/spotify.png'
			return (pic, url, url_pic)

	else:
		for item in results['tracks']['items']:
			pic = item['album']['images'][0]['url']
			url = item['external_urls']['spotify']
			url_pic = '../static/bilder/spotify.png'
			return (pic, url, url_pic)
